import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command_line = input()
        if command_line.strip().startswith("exit"):
            sys.exit(0)
        
        print(f"{command_line}: command not found")

    

if __name__ == "__main__":
    main()
