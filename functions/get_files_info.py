import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        directory_path = os.path.abspath(working_directory)
        target_directory = os.path.normpath(os.path.join(directory_path, directory))
        valid_target_directory = os.path.commonpath([directory_path, target_directory]) == directory_path
        if not valid_target_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        lines = []
        for item in os.listdir(target_directory):
            item_path = os.path.join(target_directory, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            line = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            lines.append(line)
        return "\n".join(lines)
    except Exception as error:
        return f"Error: {error}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)