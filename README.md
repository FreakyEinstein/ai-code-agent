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
