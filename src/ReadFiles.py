#!/usr/bin/python3


from os import scandir
from os.path import abspath
from configuration import dirTypeFile, formatFiles, PAHT



def ls(ruta):
    # capturamos el error si no encuentra la ruta
    try:
        return [arch.name for arch in scandir(ruta) if arch.is_file()]
    except FileNotFoundError:
        print("No existe la ruta especificada")
        raise

def lsFull(ruta):
    # capturamos el error si no encuentra la ruta
    try:
        return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
    except FileNotFoundError:
        print("No existe la ruta especificada")
        raise


def getExtension(filename):
    return filename.split(".")[-1]

def getDirTypeFile(extension):
    return formatFiles[extension]

def getDictFileCarpet(arrayFiles):
    dictFileCarpet = {}
    for file in arrayFiles:
        extension = getExtension(file)
        dirTypeFile = getDirTypeFile(extension)
        if dirTypeFile in dictFileCarpet:
            dictFileCarpet[dirTypeFile].append(file)
        else:
            dictFileCarpet[dirTypeFile] = [file]
    return dictFileCarpet

def readFilesWithFormat():
    try:
        arrayFiles = lsFull(PAHT)
        dictFileCarpet = getDictFileCarpet(arrayFiles)
        print(dictFileCarpet)
        return dictFileCarpet

    except FileNotFoundError:
        raise


