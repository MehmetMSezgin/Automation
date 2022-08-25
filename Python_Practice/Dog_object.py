from numpy import random

from Dog import Dog_class


def createDogs():
    dogNamesFile = open("names.txt", "r")
    list = dogNamesFile.readlines()
    print(list)


createDogs()

