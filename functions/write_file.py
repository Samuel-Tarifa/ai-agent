import os
from functions.validate_path import validate_path


def write_file(working_directory, file_path, content):
    try:
        if not validate_path(working_directory, file_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        file_path=os.path.join(working_directory,file_path)
        absolute_path = os.path.abspath(file_path)
        dirname = os.path.dirname(absolute_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(absolute_path, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        print(f"Error: {e}")
