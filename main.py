import os
import sys

class ShellEmulator:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.commands = {
            "ls": self.ls,
            "cd": self.cd,
            "exit": self.exit_shell
        }

    def prompt(self):
        return f"VFS ({self.current_directory}) > "

    def parse_input(self, user_input):
        parts = user_input.split()
        command = parts[0]
        arguments = parts[1:] if len(parts) > 1 else []
        return command, arguments

    def execute_command(self, command, arguments):
        # Исполнение команд
        if command in self.commands:
            self.commands[command](arguments)
        else:
            print(f"{command}: command not found")

    def ls(self, arguments):
        print(f"Executing 'ls' with arguments: {arguments}")

    def cd(self, arguments):
        if len(arguments) != 1:
            print("cd: missing argument")
        else:
            target_dir = arguments[0]
            try:
                os.chdir(target_dir)
                self.current_directory = os.getcwd()
                print(f"Changed directory to {self.current_directory}")
            except FileNotFoundError:
                print(f"cd: no such file or directory: {target_dir}")

    def exit_shell(self, arguments):
        print("Exiting shell...")
        sys.exit(0)

    def run(self):
        # Основной цикл работы оболочки
        while True:
            user_input = input(self.prompt())
            command, arguments = self.parse_input(user_input)
            self.execute_command(command, arguments)

if __name__ == "__main__":
    shell = ShellEmulator()
    shell.run()