# AI Code Agent

This project is a toy version of an "agentic" AI code editor, similar to Cursor or Claude Code, built using Google's Gemini API. It's a CLI tool that can understand a coding task and use a set of predefined functions to try and complete it.

## What Does the Agent Do?

The program is a CLI tool that:

1.  Accepts a coding task (e.g., "fix my calculator app, it's not starting correctly").
2.  Chooses from a set of predefined functions to work on the task. These functions include:
    - Scanning files in a directory.
    - Reading a file's contents.
    - Overwriting a file's contents.
    - Executing a Python script.
3.  Repeats the function-calling process until the task is complete (or it fails).

### Example Usage

Here's an example of using the agent to fix a buggy calculator app:

```bash
uv run main.py "fix my calculator app, its not starting correctly"
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

This directory contains the tools available to the AI agent.

- `get_files_info.py`: Scans the files in a directory to provide context to the agent.
- `get_file_content.py`: Reads the content of a specific file.

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
