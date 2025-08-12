import os

def validate_path(working_directory,path):
    path=os.path.join(working_directory,path)
    absolute_path=os.path.abspath(path)
    absolute_working_directory=os.path.abspath(working_directory)
    return absolute_path.startswith(absolute_working_directory)