# codecrafters test
# codecrafters test # Visit https://codecrafters.io/cli to install
# A REPL is an interactive loop that reads user input, evaluates it, prints the result, 
# and then waits for the next input.
import os
import subprocess
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
    """
    Check if command is valid
    """
    if command.command_name in built_in_commands:
        command.command_valid = True
    
    for path in path_env_list:
        if(os.path.exists(f"{path}/{command.command_name}")):
            command.command_path = f"{path}/{command.command_name}"
            command.command_valid = True
            return
    return

def type_handler(command: Command):
    """
    Type Handler (builtin)
    """
    if len(command.command_args) == 0:
        return
    elif command.command_args[0] in built_in_commands:
        sys.stdout.write(f"{command.command_args[0]} is a shell builtin\n")
    else:
        for path in path_env_list:
            if(os.path.exists(f"{path}/{command.command_args[0]}")):
                sys.stdout.write(f"{command.command_args[0]} is {path}/{command.command_args[0]}\n")
                return
        sys.stdout.write(f"{command.command_args[0]}: not found\n")
    return

def echo_handler(command: Command):
    """
    Echo Handler (builtin)
    """
    echo_string = " ".join(command.command_args)
    sys.stdout.write(f"{echo_string}\n")
    return

def exit_handler(command: Command):
    """
    Exit Handler (builtin)
    """
    if len(command.command_args) == 0:
        sys.exit(0)
    else:
        sys.exit(int(command.command_args[0]))

def execute_command(command: Command):
    """
    Run external programs with args (located using PATH environment variable)
    """
    full_command = [command.command_path] + command.command_args
    #TODO: make this more robust, add try catch and better validation
    result = subprocess.run(full_command, capture_output=True, text=True)
    sys.stdout.write(result.stdout)
    return

def command_handler(command: Command):
    """
    Command Handler that will redirect program to command executor. 
    Checks that command is valid and exists.

    :param command: command dataclass
    :return
    """
    valid_command_check(command)

    if (command.command_valid == False):
        sys.stdout.write(f"{command.command_name}: not found\n")
        return

    elif command.command_name == "exit":
        exit_handler(command)

    elif command.command_name == "echo":
        echo_handler(command)
    
    elif command.command_name == "type":
        type_handler(command)
    
    else:
        execute_command(command)

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
        sys.stdout.write("Please set the environment variable PATH\n")
        sys.exit(1)

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command_input = input()
        command_obj = command_parser(command_input)
        command_handler(command_obj)

if __name__ == "__main__":
    main()
