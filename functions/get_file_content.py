import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    """
    Reads the content of a file within a specified working directory.

    Args:
        working_directory (str): The directory where the agent is allowed to operate.
        file_path (str): The path to the file to be read, relative to the working directory.

    Returns:
        str: The content of the file, or an error message.
    """
    try:
        # Construct the full path
        base_dir = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(base_dir, file_path))

        # Security check: ensure the file is within the working directory
        if not full_path.startswith(base_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if it's a file and not a directory
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the file content
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Truncate if necessary
        if len(content) > MAX_CHARS:
            content = content[:MAX_CHARS]
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"
