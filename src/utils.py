import time

pauses = {
    ",": .2,
    ":": .2,
    ";": .2,
    ".": .4,
    "!": .4,
    "?": .4
}

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[32m"
RESET = "\033[0m"

def thinking(dots = 3):
    for i in range(dots):
        print(".", end = "", flush = True)
        time.sleep(pauses.get("."))

    print(end = '\r\033[K')

def typing(text, suffix = ""):
    for char in text + suffix:   
        if char == "\033":
            in_ansi = True

        print (char, end = "", flush = True)

        if in_ansi and char == "m":
            in_ansi = False
            continue

        if not in_ansi:
            time.sleep(pauses.get(char, .1))

def typed_print(text, dots = 3, sleep = .4):
    thinking(dots)
    time.sleep(sleep)
    typing(f'{YELLOW}{text}{RESET}')
    print()

def typed_input(text, dots = 3, sleep = .4):
    thinking(dots)
    time.sleep(sleep)
    typing(f'{YELLOW}{text}{RESET}', "\n> ")
    return input()