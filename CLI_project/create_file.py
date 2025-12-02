import requests


def create():

    filename = input("Enter the name of the file you want to create: ")
    filename = filename + ".txt"
    file = open(filename, "w")
