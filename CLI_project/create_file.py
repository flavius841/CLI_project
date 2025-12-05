import requests
import os

file = None


def main():
    print("Welcome to my CLI project. Here you cand create edit and \nfind what you want in your text file \nType 'Help' to see available commands.")
    message = input(">>>  ")
    if message.lower() == "help":
        open_help()
    elif message.lower() == "create-file":
        create()
    elif message.lower() == "upload":
        upload()
    elif message.lower() == "find":
        find_text_in_file()


def create():
    global file
    filename = input("Enter the name of the file you want to create: ")
    filename = filename + ".txt"
    file = open(filename, "a")
    file.close()


def upload():
    file = find_file()
    if file is None:
        return
    message = input("Enter the text you want to upload:  ")
    message = message.replace("\\n ", "\n")
    file.write(message)
    file.close()


def find_file():
    filename = input("Enter the name of the file you want to edit: ")
    filename = filename + ".txt"
    if os.path.exists(filename):
        print("File found! Opening it...")
        return open(filename, "a")
    else:
        print("That file does NOT exist.")
        return None


def find_text_in_file():
    filename = input("Enter the file name: ") + ".txt"
    search_text = input("Enter the text to find: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                if search_text in line:
                    print(f"Found on line {i+1}: {line.strip()}")
                    found = True
                    message = input(
                        "Do you want to replace this text? (yes/no): ")
                    if message.lower() == "yes":
                        new_text = input("Enter the new text: ")
                        lines[i] = line.replace(search_text, new_text)

            if found:
                with open(filename, "w", encoding="utf-8") as file:
                    file.writelines(lines)

            if not found:
                print("Text not found in the file.")

    except FileNotFoundError:
        print("File does not exist.")


def open_help():
    help_text = """
    Available commands:
    - create-file: Create a new text file.
    - upload: Upload text to an existing file.
        * when you upload text and want to go to a new line, use \\n
    - find: Find text in a file and optionally replace it.
    """
    print(help_text)


# def main():
#     print("Type 'Help' to see available commands.")
