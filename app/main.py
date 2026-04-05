import sys
import os
from pathlib import Path
import subprocess


def parse_line(line):
    args = []
    st = []
    in_single = False
    in_double = False
    i = 0
    stripped = line.strip()
    while i < len(stripped):
        ch = stripped[i]
        if in_single:
            if ch == "'":
                in_single = False
            else:
                st.append(ch)
        elif in_double:
            if ch == '"':
                in_double = False
            elif ch == '\\' and i + 1 < len(stripped) and stripped[i+1] in ['"','\\']:
                st.append(stripped[i + 1])
                i += 1
            else:
                st.append(ch)
        elif ch == "'":
            in_single = True
        elif ch == '"':
            in_double = True
        elif ch == '\\' and i + 1 < len(stripped):
            st.append(stripped[i + 1])
            i += 1
        elif ch == ' ':
            if st:
                args.append(''.join(st))
                st = []
        else:
            st.append(ch)
        i += 1
    if st:
        args.append(''.join(st))
    return args

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
        args = parse_line(command_line)
        if command_line.startswith("exit"):
            sys.exit(0)
        elif command_line.startswith("echo"):
            print(' '.join(args[1:]))
            continue
        elif command_line.startswith("pwd") and len(command_line.split())==1:
            current = Path(os.getcwd())
            print(f"{current}")
            continue
        elif command_line.startswith("cd"):
            new_path = Path(args[1])
            home_path = os.environ.get("HOME")
            if new_path.name =="~":
                os.chdir(home_path)
            elif new_path.exists() and new_path.is_dir():
                os.chdir(new_path)
            else:
                print(f"cd: {new_path}: No such file or directory")
        elif command_line.startswith("type"):
            command = args[1]
            exec_path = check_exec(command)
            if command in ["type", "echo", "exit", "pwd"]:
                print(f"{command} is a shell builtin")
            elif exec_path:
                print(f"{command} is {exec_path}")
            else:
                print(f"{command}: not found")
            continue
        else:
            exec_path = check_exec(args[0])
            if exec_path:
                subprocess.run(args)
            else:
                print(f"{args[0]}: command not found")
            
    
    

if __name__ == "__main__":
    main()
