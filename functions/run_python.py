import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    """
    Executes a Python file within a specified working directory.

    Args:
        working_directory (str): The directory where the agent is allowed to operate.
        file_path (str): The path to the Python file to be executed, relative to the working directory.
        args (list, optional): A list of command-line arguments to pass to the Python script. Defaults to None.

    Returns:
        str: The combined standard output and standard error of the executed script,
             or an error message if the execution fails or is not permitted.
    """
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)

        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a pyton file with the python3 interpretor. Accepts additional CLI args as an optional array, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as the CLI args for the python file.",
                items=types.Schema(
                    type=types.Type.STRING
                )
            )
        },
    ),
)
