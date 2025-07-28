import os
from config import MAX_SIZE


def get_file_content(working_directory, file_path):
    try:
        file_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(file_path)
        absolute_working_path = os.path.abspath(working_directory)
        if not absolute_path.startswith(absolute_working_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(absolute_path, "r") as f:
            content = f.read(MAX_SIZE)

        if len(content) == MAX_SIZE:
            content += f'[...File "{absolute_path}" truncated at 10000 characters]'

    except Exception as e:
        return f"Error: {e}"

    return content
