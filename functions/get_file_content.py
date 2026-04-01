import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        directory_path = os.path.abspath(working_directory)
        target_directory = os.path.normpath(os.path.join(directory_path, file_path))
        valid_target_directory = os.path.commonpath([directory_path, target_directory]) == directory_path
        if not valid_target_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_directory):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_directory, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    except Exception as error:
        return f"Error: {error}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the file contents of the selected file_path inside a working_directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path that is meant to be read relative to the working directory",
            ),
        },
        required = ["file_path"],
    ),
)