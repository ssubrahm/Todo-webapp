# Function to read from a file of todos into  a list
import os
import sys

FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """ Read as input the text file specified by the filepath argument
        and return a list of todo items"""

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILE_PATH):
    """ Take as input a list of todo items and write them into the file
    specified in the filepath argument to the function"""

    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename
