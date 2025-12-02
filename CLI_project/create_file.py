import requests

file = None


def create():

    filename = input("Enter the name of the file you want to create: ")
    filename = filename + ".txt"
    file = open(filename, "a")


def upload():
    file = find_file()
    message = input("Enter the text you want to upload: ")
    message = "\n" + message
    file.write(message)


def find_file():
    filename = input("Enter the name of the file you want to edit: ")
    filename = filename + ".txt"
    return open(filename, "a")
