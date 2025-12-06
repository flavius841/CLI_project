import requests
import os
from colorama import init, Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


file = None
init(autoreset=True)
commnads = ["help", "create-file", "upload",
            "find", "count", "rename", "exit"]
commands_find = ["yes", "no", "replace-everywhere",
                 "delete", "delete-everywhere"]
command_completer = WordCompleter(commnads, ignore_case=True)
find_completer = WordCompleter(commands_find, ignore_case=True)


def main():
    print("Welcome to my CLI project. Here you cand create edit and \nfind what you want in your text "
          "file \nType 'help' to see available commands or read more information.")

    while True:
        message = prompt(">>> ", completer=command_completer).strip()

        if message.lower() == "help":
            open_help()

        elif message.lower() == "create-file":
            create()

        elif message.lower() == "upload":
            upload()

        elif message.lower() == "find":
            find_text_in_file()

        elif message.lower() == "count":
            Count()

        elif message.lower() == "rename":
            rename_file()

        elif message.lower() == "delete":
            delete_file()

        elif message.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        elif message.strip().lower() != "":
            print("Invalid command. Type 'Help' to see available commands.")


def create():
    global file
    filename = input("Enter the name of the file you want to create: ")
    filename = filename + ".txt"
    file = open(filename, "a")
    file.close()
    print(f"File {filename} created successfully!")


def upload():
    file = find_file()
    if file is None:
        return
    message = input("Enter the text you want to upload:  ")
    message = message.replace("\\n ", "\n")
    file.write(message)
    file.close()
    print("Text uploaded successfully!")


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
    replace_all = False
    message = ""

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                if search_text in line:
                    print(f"Found on line {i+1}: {line.strip()}")
                    found = True

                    if not replace_all:
                        message = prompt(
                            "Do you want to replace this text? (yes/no/replace-everywhere/delete/delete-everywhere): ",
                            completer=find_completer).strip()

                    if message.lower() == "yes" or not replace_all:
                        new_text = input("Enter the new text: ")
                        lines[i] = line.replace(search_text, new_text)

                    if message.lower() == "everywhere":
                        replace_all = True
                        lines[i] = line.replace(search_text, new_text)

            if found:
                with open(filename, "w", encoding="utf-8") as file:
                    file.writelines(lines)

            if not found:
                print("Text not found in the file.")

    except FileNotFoundError:
        print("File does not exist.")


def open_help():
    help_text = f"""
    {Fore.CYAN}Available commands:{Style.RESET_ALL}
    {Fore.GREEN}- create-file:{Style.RESET_ALL} Create a new text file.
    {Fore.YELLOW}- upload:{Style.RESET_ALL} Upload text to an existing file.
        * when you upload text and want to go to a new line, use \\n
    {Fore.MAGENTA}- find:{Style.RESET_ALL} Find text in a file and optionally replace it.
    {Fore.BLUE}- count:{Style.RESET_ALL} Count words, lines, or characters in a file.
    {Fore.RED}- exit:{Style.RESET_ALL} Exit the program.
    {Fore.BLACK}- rename:{Style.RESET_ALL} Rename an existing file.
    {Fore.LIGHTRED_EX}- delete:{Style.RESET_ALL} Delete an existing file.

    {Fore.CYAN}Note:{Style.RESET_ALL} This CLI only works in the folder you are currently in.

    """
    print(help_text)


def Count():
    filename = input("Enter the file name: ") + ".txt"
    message = input("Do you want to count (words/lines/characters): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if message.lower() == "lines":
                print(f"The file has {len(lines)} lines.")
            elif message.lower() == "characters":
                char_count = 0
                message2 = input(
                    "Do you want to count spaces as well? (yes/no): ")
                if message2.lower() == "yes":
                    spcace_included = True
                else:
                    spcace_included = False
                for line in lines:
                    if spcace_included:
                        char_count = char_count + len(line)
                    else:
                        line_without_spaces = line.replace(
                            " ", "").replace("\n", "")
                        char_count = char_count + len(line_without_spaces)
                print(f"The file has {char_count} characters.")
            elif message.lower() == "words":
                word_count = 0
                for line in lines:
                    words = line.split()
                    word_count = word_count + len(words)
                print(f"The file has {word_count} words.")
            else:
                print("Invalid option. Please choose words, lines, or characters.")
    except FileNotFoundError:
        print("File does not exist.")


def rename_file():
    old_filename = input("Enter the current file name: ") + ".txt"
    if not os.path.exists(old_filename):
        print("File does not exist.")
        return
    new_filename = input("Enter the new file name: ") + ".txt"
    os.rename(old_filename, new_filename)
    print(f"File renamed to {new_filename} successfully!")


def delete_file():
    filename = input(
        "Enter the name of the file you want to delete: ") + ".txt"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File {filename} deleted successfully!")
    else:
        print("File does not exist.")
