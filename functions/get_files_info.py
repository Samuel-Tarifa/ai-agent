import os
def get_files_info(working_directory, directory="."):
    try:
        directory=os.path.join(working_directory,directory)
        absolute_path=os.path.abspath(directory)
        absolute_working_path=os.path.abspath(working_directory)
        if not absolute_path.startswith(absolute_working_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
        contents=os.listdir(absolute_path)
        info=""
        for name in contents:
            path=os.path.join(absolute_path,name)
            size=os.path.getsize(path)
            is_dir=os.path.isdir(path)
            info+=f"- {name}: file_size={size} bytes, is_dir={is_dir}\n"
    except Exception as e:
        return f"Error: {e}"

    return info

