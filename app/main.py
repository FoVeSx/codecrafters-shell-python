# codecrafters test
# codecrafters test # Visit https://codecrafters.io/cli to install
# A REPL is an interactive loop that reads user input, evaluates it, prints the result, 
# and then waits for the next input.
import sys

valid_commands = ["echo", "cd", "ls", "exit"]

def command_handler(command: str, options: list):
    """
    Command Handler that will redirect program to command executor. 
    Checks that command is valid and exists.

    :param command: string of the command (program) to be ran
    :param options: list of arguments passed into command
    :return
    """
    if command not in valid_commands:
        sys.stdout.write(f"{command}: command not found\n")
        return

    if command == "exit":
        if len(options) == 0:
            sys.exit(0)
        else:
            sys.exit(int(options[0]))

    return

def command_parser(command_line: str):
    """
    Parse the entire command for the command and its options.
    
    :param command_line: string of the entire command line inputted
    :return tuple: command string and options list
    """
    command_list = command_line.split(" ")
    command = command_list[0]
    options = command_list[1:]
    return command, options

def main():
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command_input = input()
        command, options = command_parser(command_input)
        command_handler(command, options)

if __name__ == "__main__":
    main()
