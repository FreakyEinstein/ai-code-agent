# AI Code Agent

This project is a simple, command-line "agentic" AI code editor built using Google's Gemini API. It's a toy version of tools like Cursor or the agentic features in Claude, designed to demonstrate the core principles of an AI agent that can interact with a local filesystem to complete coding tasks.

## How it Works

The agent operates in a loop, allowing it to reason, act, and observe the results of its actions, refining its approach until the user's request is fulfilled.

The process is as follows:

1.  **Prompt:** The user provides a high-level coding task via the command line.
2.  **Reasoning:** The Gemini model receives the prompt, the conversation history, and a list of available tools. It decides which tool to use to get closer to the goal.
3.  **Action:** The agent executes the chosen function (e.g., `get_file_content`). All actions are sandboxed and restricted to a specific working directory (`calculator/` in this project) for security.
4.  **Observation:** The output of the function (e.g., file contents or an error message) is sent back to the model.
5.  **Repeat:** The model takes the new information into account and goes back to step 2, choosing the next best action. This loop continues until the agent believes the task is complete or it hits a maximum iteration limit.
6.  **Response:** The agent provides a final, textual response to the user summarizing the work done.

## Getting Started

Follow these steps to get the AI agent running on your local machine.

### Prerequisites

- Python 3.10+
- uv - A fast Python project and package manager.
- Git for cloning the repository.
- Access to a Unix-like shell (e.g., zsh or bash).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd ai-code-agent
    ```

2.  **Install dependencies:**
    This project uses `google-generativeai` to interact with the Gemini API and `python-dotenv` for managing environment variables.
    ```bash
    uv pip install google-generativeai python-dotenv
    ```

### Configuration

The agent requires an API key from Google to use the Gemini model.

1.  **Get a Gemini API Key:**
    Visit Google AI Studio to create your free API key.

2.  **Create a `.env` file:**
    In the root of the project directory, create a file named `.env` and add your API key to it:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
    The application uses the `dotenv` library to load this key automatically.

## Usage

You can run the agent from your terminal using `uv`. The agent is hardcoded to operate within the `calculator/` directory.

### Basic Command

Provide your coding task as a string argument.

```bash
uv run main.py "fix the bug in my calculator where it doesn't handle parentheses"
```

The agent would then proceed to call functions to understand and fix the code, showing output like this:

```
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

## Prerequisites

- Python 3.10+
- [uv](httpss://github.com/astral-sh/uv) project and package manager
- Access to a Unix-like shell (e.g., zsh or bash)

## Core Components

### `main.py`

This is the main entry point for the AI agent. It takes a user's prompt and uses an LLM to orchestrate calls to various functions to accomplish the task.

### `functions/`

This directory houses the functional tools the AI agent utilizes to interact with the file system and perform coding tasks. Each file within this directory defines a specific capability, adhering to a consistent structure that includes a function definition and a corresponding schema for interaction with the Gemini API.

#### `get_files_info.py`

This module provides the `get_files_info` function, which lists the files and subdirectories within a specified directory, providing essential context to the agent about the file system structure.

**Function:** `get_files_info(working_directory, directory=".")`

- **Description:** Lists files in the specified directory along with their sizes and directory status, constrained to the working directory.
- **Parameters:**
  - `working_directory` (str): The base directory where the agent is allowed to operate.
  - `directory` (str, optional): The directory to list files from, relative to the working directory. Defaults to the working directory itself.
- **Returns:** A string containing a list of files with their sizes and directory status or an error message if the directory is inaccessible or outside the working directory.

#### `get_file_content.py`

This module contains the `get_file_content` function, which retrieves the content of a file.

**Function:** `get_file_content(working_directory, file_path)`

- **Description:** Retrieves the contents of a specified file as a string, with access constrained to the working directory.
- **Parameters:**
  - `working_directory` (str): The directory where the agent is permitted to operate.
  - `file_path` (str): The path to the file to be read, relative to the working directory.
- **Returns:** The content of the file as a string, truncated to `MAX_CHARS` if necessary, or an error message.

#### `write_file.py`

This module includes the `write_file` function, enabling the agent to modify files within the designated working directory.

**Function:** `write_file(working_directory, file_path, content)`

- **Description:** Writes content to a file within the specified working directory, overwriting existing files or creating new ones as needed.
- **Parameters:**
  - `working_directory` (str): The directory where the agent is authorized to perform file operations.
  - `file_path` (str): The path to the file to be written, relative to the working directory.
  - `content` (str): The content to write to the file.
- **Returns:** A success message or an error message if the write operation fails or the file path is outside the permitted working directory.

#### `run_python.py`

This module enables the agent to execute Python files within the designated working directory.

**Function:** `run_python_file(working_directory, file_path, args=None)`

- **Description:** Executes a Python file within a specified working directory.
- **Args:**
  - `working_directory` (str): The directory where the agent is allowed to operate.
  - `file_path` (str): The path to the Python file to be executed, relative to the working directory.
  - `args` (list, optional): A list of command-line arguments to pass to the Python script. Defaults to None.
- **Returns:**
  - str: The combined standard output and standard error of the executed script,
    or an error message if the execution fails or is not permitted.

### `calculator/`

This is a sample Python application that the AI agent can interact with and modify. It's a simple command-line calculator.

## How to Run

### Running the Agent

To run the AI agent, use `uv`:

```bash
uv run main.py "Your coding task here"
```

### Running Tests

To run the tests for the agent's functions:

```bash
uv run tests.py
```
