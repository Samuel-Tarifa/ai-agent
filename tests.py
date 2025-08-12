from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


def main():
    cases = [
        run_python_file("calculator", "main.py"),
        run_python_file("calculator", "main.py", ["3 + 5"]),
        run_python_file("calculator", "tests.py"),
        run_python_file("calculator", "../main.py"),
        run_python_file("calculator", "nonexistent.py"),
    ]

    for case in cases:
        print(case)


if __name__ == "__main__":
    main()
