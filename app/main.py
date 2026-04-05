import sys
import os
from pathlib import Path

def check_exec(command):
    paths = os.environ.get("PATH")
    paths = paths.split(":")
    for p in paths:
        current_path = Path(p)
        if current_path.exists() and current_path.is_dir():
            files = current_path.iterdir()
            for f in files:
                file_path = current_path / f
                if f.name == command and os.access(file_path,os.X_OK):
                    return file_path
    return False
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
        elif command_line.startswith("type"):
            command = command_line.split()[1]
            exec_path = check_exec(command)
            if command in ["type", "echo", "exit"]:
                print(f"{command} is a shell builtin")
            elif exec_path:
                print(f"{command} is {exec_path}")
            else:
                print(f"{command}: not found")
            continue
        else:    
            print(f"{command_line}: command not found")
            
    
    

if __name__ == "__main__":
    main()
