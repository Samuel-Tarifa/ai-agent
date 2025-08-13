import os
from dotenv import load_dotenv
from google import genai
import sys
import time

from available_functions import available_functions
from call_function import call_function


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

All paths you provide should be relative to the working directory, so they may start with './', your working directory is calculator. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

config = types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

verbose = "--verbose" in sys.argv

count = 0
from config import ITERATIONS_LIMIT

while count < ITERATIONS_LIMIT:

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=messages, config=config
        )
        if response.text and not response.function_calls:
            print(response.text)
            break

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                function_call_result = call_function(
                    function_call_part, verbose=verbose
                )
                if not function_call_result.parts[0].function_response.response:
                    raise Exception("Function call failed")
                response_dict = function_call_result.parts[0].function_response.response
                response_result = response_dict[list(response_dict.keys())[0]]
                if verbose:
                    print(f"-> {response_result}")
                new_message = types.Content(
                    role="user", parts=[types.Part(text=response_result)]
                )
                messages.append(new_message)

    except Exception as e:
        print("Error: ", e)

    count += 1
    time.sleep(1)

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
