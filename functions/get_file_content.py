import os
from config import MAX_SIZE
from functions.validate_path import validate_path


def get_file_content(working_directory, file_path):
    try:
        if not validate_path(working_directory,file_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        file_path=os.path.join(working_directory,file_path)
        absolute_path = os.path.abspath(file_path)
        if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(absolute_path, "r") as f:
            content = f.read(MAX_SIZE)

        if len(content) == MAX_SIZE:
            content += f'[...File "{absolute_path}" truncated at 10000 characters]'

    except Exception as e:
        return f"Error: {e}"

    return content
