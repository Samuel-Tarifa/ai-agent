from functions.validate_path import validate_path
import os,subprocess

def run_python_file(working_directory, file_path, args=[]):
    if not validate_path(working_directory,file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    absolute_path=os.path.abspath(os.path.join(working_directory,file_path))
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result=subprocess.run(
            ["python3", f"{file_path}"]+args,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )
        stdout="STDOUT:\n"+result.stdout if len(result.stdout)>0 else "No output produced."
        stderr="STDERR: "+result.stderr if len(result.stderr)>0 else "No error produced."
        info=stdout+"\n"+stderr+"\n"
        if result.returncode!=0:
            info+=f"Process exited with code {result.returncode}"
        return info
    except Exception as e:
        return f"Error: executing Python file: {e}"