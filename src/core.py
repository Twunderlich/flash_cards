from src.utils import typed_print

class Engine(object):
    def __init__(self):
        self.running = False
        self.boxes = {
            "python": {
                "What keyword defines a function?": "def",
                "What file marks a folder as a package?": "__init__.py",
                "Are strings mutable or immutable?": "immutable"
            },
            "git": {
                "What command creates an empty file?": "touch",
                "What file tells Git what to ignore?": ".gitignore",
                "How do you check repo status?": "git status"
            }
        }
        self.commands ={
            "quit": self.quit,
            "help": self.help,
            "practice": self.practice
        }

    def practice(self):
        if not self.boxes:
            typed_print("There are no boxes to practice")
            return

        else:
            typed_print("Box options: ")

            count = 1
            for key in self.boxes:
                typed_print(f"{count}) {key}", 0, 0)
                count=+ 1

        user_input = input("> ")

        box = self.boxes.get(user_input)

        if box:
            typed_print(f'Starting {user_input}')
        else: 
            typed_print("Invalid option.")
            return

    def help(self):
        typed_print("Command options: ") 

        count = 1
        for key in self.commands:
            typed_print(f"{count}) {key}", 0, 0)
            count += 1

    def quit(self):
        typed_print("Goodbye")
        self.running = False

    def start(self):
        typed_print("Welcome to Flash Cards", 0)
        self.running = True

        while self.running:
            user_input = input("> ").strip().lower()

            action = self.commands.get(user_input)
            if action:
                action() 
            else:
                typed_print("Invalid choice.")
