import os
import sys
import argparse
import google.genai as genai
from google.genai import types
from dotenv import load_dotenv

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file

from call_functions import call_function


def main():
    load_dotenv()

    # Use argparse for robust command-line argument parsing
    parser = argparse.ArgumentParser(
        description="A simple command-line AI agent using Google Gemini."
    )
    parser.add_argument("prompt", help="The prompt to send to the AI model.")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output."
    )
    args = parser.parse_args()

    system_prompt = """
        You are a helpful AI coding agent.
        You can make multiple function calls to achieve the user's goal.
        When a user asks a question or makes a request, think step-by-step and use the available tools to answer the request.
        You can perform the following operations:
        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files
        When the user asks to work on a any changes or asks to fix, the project is always available in the WORKING_DIR value.
        Before you finalise the results, you need to test all the scenarios if new tests are to needed then include new test cases in the unit tests.
        Also you have to run the files to test if it works as expected or not.
        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        Once you have the final answer, provide it in a clear and concise way.
        """

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )

    try:
        # Use the newer genai configuration and add error handling for the API key
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Please set it in your .env file or environment.")
        client = genai.Client(api_key=api_key)

        messages = [
            types.Content(role="user", parts=[types.Part(text=args.prompt)]),
        ]

        MAX_ITERS = 20
        for i in range(MAX_ITERS):
            if args.verbose:
                print(f"\n--- Iteration {i+1}/{MAX_ITERS} ---")

            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                ),
            )

            if not response.candidates:
                print("No response from model, exiting.")
                break

            # Add the model's response to the conversation history.
            messages.append(response.candidates[0].content)

            # Print verbose information if the flag is set
            if args.verbose and response.usage_metadata:
                print("\n--- Verbose Info ---")
                print(
                    f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(
                    f"Response tokens: {response.usage_metadata.candidates_token_count}")
                print(
                    f"Total tokens: {response.usage_metadata.total_token_count}")

            # If there are no function calls, the model has given its final answer.
            if not response.function_calls:
                print(f"Final response:\n{response.text}")
                break

            # Execute the function calls.
            function_response_parts = []
            for function_call_part in response.function_calls:
                function_call_result = call_function(
                    function_call_part, args.verbose)
                if args.verbose:
                    print(
                        f"-> {function_call_result.parts[0].function_response.response}")
                # Collect the function response part.
                function_response_parts.append(function_call_result.parts[0])

            if function_response_parts:
                # Add the function call results to the conversation history as a single message.
                messages.append(types.Content(
                    role="tool", parts=function_response_parts))
        else:
            print("Agent reached max iterations, exiting.")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
