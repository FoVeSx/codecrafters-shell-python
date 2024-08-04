# codecrafters test
# codecrafters test # Visit https://codecrafters.io/cli to install
# A REPL is an interactive loop that reads user input, evaluates it, prints the result, 
# and then waits for the next input.


import sys

def main():
    valid_commands = ["echo", "cd", "ls", "exit"]

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()

        if command not in valid_commands:
            sys.stdout.write(f"{command}: command not found\n")

        if command == "exit":
            break

if __name__ == "__main__":
    main()
