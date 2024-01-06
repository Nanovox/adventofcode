import os.path as path


def read_lines(filename):
    lines = []
    file = open(path.abspath(filename), "r")
    lines = file.readlines()
    file.close()
    return lines
