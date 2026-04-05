import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command_line = input()
        command_line = command_line.strip()
        if command_line.startswith("exit"):
            sys.exit(0)
        elif command_line.startswith("echo"):
            to_print = command_line.split("echo ")[1]
            print(to_print)
            continue
        print(f"{command_line}: command not found")

    

if __name__ == "__main__":
    main()
