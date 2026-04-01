import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", abs_file_path]
        if args is not None:
            command.extend(args)
        completed = subprocess.run(
            command,
            cwd = abs_working_dir,
            capture_output = True,
            text = True,
            timeout = 30
        )
        output = []
        if completed.returncode != 0:
            output.append(f"Process exited with code {completed.returncode}")
        if completed.stdout == "" and completed.stderr == "":
            output.append("No output produced")
        if completed.stdout != "":
            output.append(f"STDOUT: {completed.stdout}")
        if completed.stderr != "":
            output.append(f"STDERR: {completed.stderr}")
        return "\n".join(output)
    except Exception as error:
        return f"Error: executing Python file: {error}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path that is meant to be read relative to the working directory",
            ),
            "args": types.Schema(
                type = types.Type.ARRAY,
                items = types.Schema(type = types.Type.STRING),
                description="Optional list of arguments to path to the Python file",
            ),
        },
        required = ["file_path"],
    ),
)