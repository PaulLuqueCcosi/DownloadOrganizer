#!/usr/bin/python3
from ReadFiles import readFilesWithFormat
from MoveFiles import moveFiles

if __name__ == "__main__":
    try:
        dictFilesDir = readFilesWithFormat()
    except FileNotFoundError:
        print("Error")

    # move files
    moveFiles(dictFilesDir)