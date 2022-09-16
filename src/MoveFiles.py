import os
import shutil
from Configuration import PAHT

# create a function to make a directory
def makeDir(dictFilerFormat, newDir = PAHT):

    for folder in dictFilerFormat.keys():
        pathNewDir = os.path.join(newDir, folder) 
        if not os.path.exists(pathNewDir):
            os.mkdir(pathNewDir)
            print("Created directory: ", pathNewDir)
    return

def moveFiles(dictFilerFormat, newDir = PAHT):

    makeDir(dictFilerFormat)

    for folder, file in dictFilerFormat.items():
        pathNewDir = os.path.join(newDir, folder) 
        for f in file:
            fileName = os.path.basename(f)
            pathNewFile = os.path.join(pathNewDir, fileName)

            shutil.move(f, pathNewFile)
            print("Moved file: ", pathNewFile)
    return

