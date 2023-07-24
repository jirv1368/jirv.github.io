import os
import sys

# This will get the current working directory
# os.listdir() function gets a list of all files and directories in the current directory
# A message to indicate  it is listing the contents of the current directory
def list_directory():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    print("Contents of the current directory:")
    for file in files:
        print(file)

# This function adds the two parameters together and stores the result in a variable called result.
# It uses an f-string to print the result.
def add_numbers(a, b):
    result = a + b
    print(f"Result: {result}")

# This will display a list of commands
def show_help():
    print("Available commands:")
    print("LIST - List the contents of the current directory")
    print("ADD a b - Add two numbers together (a and b)")
    print("HELP - Show a list of available commands")
    print("EXIT - Exit the shell")


# This is the command-line interface for interacting with the computer
# The main functio contains a loop
# The user can enter various commands
def main():
    while True:
        command = input("Enter a command: ").strip()
        command_parts = command.split()

        if command_parts[0].upper() == "LIST":
            list_directory()
        elif command_parts[0].upper() == "ADD":
            if len(command_parts) == 3:
                try:
                    a = float(command_parts[1])
                    b = float(command_parts[2])
                    add_numbers(a, b)
                except ValueError:
                    print("Invalid input. Please provide two numbers.")
            else:
                print("Invalid input. ADD command expects two numbers.")
        elif command_parts[0].upper() == "HELP":
            show_help()
        elif command_parts[0].upper() == "EXIT":
            print("Exiting shell...")
            sys.exit(0)
        else:
            print("Invalid command. Type HELP for a list of available commands.")


if __name__ == "__main__":
    main()
