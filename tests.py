from functions.get_files_info import get_files_info


def run_manual_tests():
    """
    Runs a series of manual tests on the get_files_info function
    and prints the output for debugging purposes.
    """
    # The working directory for the agent is the project root.
    working_directory = "."

    print("--- Testing get_files_info function ---")

    print("\n[1] Listing contents of the root working directory:")
    print(get_files_info(working_directory=working_directory))

    print("\n[2] Listing contents of the 'calculator' subdirectory:")
    print(get_files_info(working_directory=working_directory, directory="calculator"))

    print("\n[3] Listing contents of a nested subdirectory 'calculator/pkg':")
    print(get_files_info(working_directory=working_directory,
          directory="calculator/pkg"))

    print("\n[4] Attempting to list a non-existent directory:")
    print(get_files_info(working_directory=working_directory,
          directory="does_not_exist"))

    print("\n[5] Attempting to list a directory outside the working directory:")
    # We set 'calculator' as the working dir and try to access its parent.
    print(get_files_info(working_directory="calculator", directory=".."))

    print("\n--- Tests complete ---")


if __name__ == "__main__":
    run_manual_tests()
