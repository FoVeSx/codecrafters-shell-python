# codecrafters test
# codecrafters test # Visit https://codecrafters.io/cli to install
# A REPL is an interactive loop that reads user input, evaluates it, prints the result, 
# and then waits for the next input.
import os
import sys

from dataclasses import dataclass

built_in_commands = ["echo", "exit", "type"]
path_env_list = []

@dataclass
class Command:
    command_name: str
    command_args: list
    command_path: str
    command_valid: bool

def valid_command_check(command: Command):
    if command.command_name in built_in_commands:
        command.command_valid = True
    
    for path in path_env_list:
        if(os.path.exists(f"{path}/{command.command_name}")):
            command.command_path = f"{path}/{command.command_name}"
            command.command_valid = True
            return
    return

def type_handler(command: Command):
    if len(command.command_args) == 0:
        return
    elif command.command_args[0] in built_in_commands:
        print(f"{command.command_args[0]} is a shell builtin")
    else:
        for path in path_env_list:
            if(os.path.exists(f"{path}/{command.command_args[0]}")):
                print(f"{command.command_args[0]} is {path}/{command.command_args[0]}")
                return
        print(f"{command.command_args[0]}: not found")
    return

def echo_handler(command: Command):
    echo_string = " ".join(command.command_args)
    print(echo_string)
    return

def exit_handler(command: Command):
    if len(command.command_args) == 0:
        sys.exit(0)
    else:
        sys.exit(int(command.command_args[0]))

def command_handler(command: Command):
    """
    Command Handler that will redirect program to command executor. 
    Checks that command is valid and exists.

    :param command: command dataclass
    :return
    """
    valid_command_check(command)
    if (command.command_valid == False):
        print(f"{command.command_name}: not found")
        return

    if command.command_name == "exit":
        exit_handler(command)
        # exit, no return
    
    if command.command_name == "echo":
        echo_handler(command)
        return
    
    if command.command_name == "type":
        type_handler(command)

    return

def command_parser(command_line: str):
    """
    Parse the entire command for the command and its options.
    
    :param command_line: string of the entire command line inputted
    :return Command: command dataclass
    """
    command_list = command_line.split(" ")

    command_name = command_list[0]
    args_list = command_list[1:]

    return Command(command_name, args_list, "", False)

def main():
    global path_env_list

    try:
        path_env_str = os.environ["PATH"]
        path_env_list = path_env_str.split(":")

    except KeyError:
        print("Please set the environment variable PATH")
        sys.exit(1)

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command_input = input()
        command_obj = command_parser(command_input)
        command_handler(command_obj)

if __name__ == "__main__":
    main()
