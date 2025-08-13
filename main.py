import os
from dotenv import load_dotenv
from google import genai
import sys
from functions.get_file_content import get_file_content

from available_functions import available_functions


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Error: prompt not provided")
    exit(1)

user_prompt = sys.argv[1]

from google.genai import types

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

config = types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=messages, config=config
)

from call_function import call_function

verbose="--verbose" in sys.argv

if response.function_calls:
    for function_call_part in response.function_calls:
        function_call_result=call_function(function_call_part,verbose=verbose)
        if not function_call_result.parts[0].function_response.response:
            raise Exception("Function call failed")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

print(response.text)

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
