import os
import sys
import argparse
import google.genai as genai
from google.genai import types
from dotenv import load_dotenv

from functions.get_files_info import get_files_info


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
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,

        )

        print(response.text)

        # Print verbose information if the flag is set
        if args.verbose and hasattr(response, 'usage_metadata') and response.usage_metadata:
            print("\n--- Verbose Info ---")
            print(f"User Prompt: {args.prompt}")
            print(
                f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(
                f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print(f"Total tokens: {response.usage_metadata.total_token_count}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    print(get_files_info("calculator"))
