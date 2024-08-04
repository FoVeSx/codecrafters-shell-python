# codecrafters test
# codecrafters test # Visit https://codecrafters.io/cli to install
# A REPL is an interactive loop that reads user input, evaluates it, prints the result, 
# and then waits for the next input.
import sys

valid_commands = ["cd", "echo", "exit", "ls", "type"]

def type_handler(options: list):
    if len(options) == 0:
        return
    elif options[0] not in valid_commands:
        print(f"{options[0]}: not found")
    else:
        print(f"{options[0]} is a shell builtin")
    return

def echo_handler(options: list):
    echo_string = " ".join(options)
    print(echo_string)
    return

def command_handler(command: str, options: list):
    """
    Command Handler that will redirect program to command executor. 
    Checks that command is valid and exists.

    :param command: string of the command (program) to be ran
    :param options: list of arguments passed into command
    :return
    """
    if command == "exit":
        if len(options) == 0:
            sys.exit(0)
        else:
            sys.exit(int(options[0]))

    if command not in valid_commands:
        sys.stdout.write(f"{command}: command not found\n")
        return
    
    if command == "echo":
        echo_handler(options)
        return
    
    if command == "type":
        type_handler(options)

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
