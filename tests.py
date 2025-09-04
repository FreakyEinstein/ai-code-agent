from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


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

    print("\n--- get_files_info tests complete ---")


def test_get_file_content():
    """
    Tests the get_file_content function with various cases.
    """
    print("\n--- Testing get_file_content function ---")

    print("\n[1] Reading a file that exists:")
    print(get_file_content("calculator", "main.py"))

    print("\n[2] Reading a nested file that exists:")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\n[3] Attempting to read a file outside the working directory:")
    print(get_file_content("calculator", "/bin/cat"))

    print("\n[4] Attempting to read a non-existent file:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

    print("\n--- get_file_content tests complete ---")


def test_write_file():
    """
    Tests the write_file function with various cases.
    """
    print("\n--- Testing write_file function ---")

    print("\n[1] Writing to a file:")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("\n[2] Writing to a new file in a nested directory:")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print("\n[3] Attempting to write to a file outside the working directory:")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print("\n--- write_file tests complete ---")


if __name__ == "__main__":
    # run_manual_tests()
    # test_get_file_content()
    test_write_file()
