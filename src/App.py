#!/usr/bin/python3
from ReadFiles import readFilesWithFormat

if __name__ == "__main__":
    try:
        dictFilesDir = readFilesWithFormat()
    except FileNotFoundError:
        print("Error")

