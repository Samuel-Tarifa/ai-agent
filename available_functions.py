from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content=types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of the file in plain text, constraint to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to get the content, relative to the working directory.",
            ),
        },
        required=["file_path"]
    ),
)

schema_run_python_file=types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a .py file, constraint to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to run, relative to the working directory.",
            ),
            "args":types.Schema(
                type=types.Type.ARRAY,
                description="Args to run the file, if arguments are not provided, it may not need it, defaults to an empty array.",
                items=types.Schema(type=types.Type.STRING)
            )
        },
        required=["file_path"],
    ),
)

schema_write_file=types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, constraint by the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory, if file not exists, it creates it.",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="Content that will be writen into the file."
            )
        },
        required=["file_path","content"],
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)