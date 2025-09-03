import os


def get_files_info(working_directory: str, directory=None):
    absolute_working_dir = os.path.abspath(working_directory)

    if directory:
        absolute_directory = os.path.abspath(
            os.path.join(absolute_working_dir, directory))
        display_dir = directory
    else:
        absolute_directory = absolute_working_dir
        display_dir = "."  # For error messages

    if not os.path.isdir(absolute_directory):
        return f'Error: "{display_dir}" is not a directory'

    if not absolute_directory.startswith(absolute_working_dir):
        return f'Error: Cannot list "{display_dir}" as it is outside the permitted working directory'

    response_lines = []
    # Sort contents for consistent output
    contents = sorted(os.listdir(absolute_directory))

    for content in contents:
        content_path = os.path.join(absolute_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        response_lines.append(
            f"- {content}: file_size={size} bytes, is_dir={is_dir}")

    return "\n".join(response_lines)
