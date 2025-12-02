import requests
import os

file = None


def create():

    filename = input("Enter the name of the file you want to create: ")
    filename = filename + ".txt"
    file = open(filename, "a")


def upload():
    file = find_file()
    if file is None:
        return
    message = input("Enter the text you want to upload:  ")
    file.write(message)


def find_file():
    filename = input("Enter the name of the file you want to edit: ")
    filename = filename + ".txt"
    if os.path.exists(filename):
        print("File found! Opening it...")
        return open(filename, "a")
    else:
        print("That file does NOT exist.")
        return None


def open_help():
    help_text = """
    Available commands:
    - create-file: Create a new text file.
    - upload: Upload text to an existing file.
        * when you upload text and want to go to a new line, use \\n
    """
    print(help_text)


# def main():
#     print("Type 'Help' to see available commands.")
