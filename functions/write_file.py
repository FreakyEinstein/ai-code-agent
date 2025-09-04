import os

def write_file(working_directory, file_path, content):
    """
    Writes content to a file within a specified working directory.

    Args:
        working_directory (str): The directory where the agent is allowed to operate.
        file_path (str): The path to the file to be written, relative to the working directory.
        content (str): The content to write to the file.

    Returns:
        str: A success message or an error message.
    """
    try:
        base_dir = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(base_dir, file_path))

        # Security check: ensure the file is within the working directory
        if not full_path.startswith(base_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}"'

    except Exception as e:
        return f"Error: {e}"