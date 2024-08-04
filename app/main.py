# codecrafters test
# codecrafters test # Visit https://codecrafters.io/cli to install

import sys

def main():
    valid_commands = ["echo", "cd", "ls"]

    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    if command not in valid_commands:
        sys.stdout.write(f"{command}: command not found")

if __name__ == "__main__":
    main()
