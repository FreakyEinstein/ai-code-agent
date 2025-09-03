from google import genai
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    print(response.text)

    if response is not None or response.usage_metadata is not None:
        print(f"Prompt tokens : {response.usage_metadata.prompt_token_count}")
        print(
            f"Response tokens : {response.usage_metadata.candidates_token_count}")
    else:
        print("Response is None")
        return


main()
