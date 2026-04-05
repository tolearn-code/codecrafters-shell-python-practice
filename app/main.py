import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command_line = input()
        print(f"{command_line}: command not found")
    

if __name__ == "__main__":
    main()
