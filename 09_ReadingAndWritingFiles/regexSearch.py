import re
import os
from pathlib import Path

to_print = []
line = []

folderPath = input("Enter destination of folder: \n")

x = input("Enter phrase/pattern to search: \n")

item = re.compile(x)

# path = os.getcwd()
path = folderPath

allfiles = os.listdir(path) #list

for fileName in allfiles:

    if fileName.endswith(".txt"):

        my_file = open(Path(path)/fileName)

        for eachLine in my_file.readlines():
            phrases = item.findall(eachLine)

            for phrase in phrases:
                to_print.append(phrase)
                line.append(eachLine)
                break


        my_file.close()

if to_print != []:
    print("Matches Found: ", end ='')
    print(to_print)
    print("Matches found in lines: ", end = '')
    print(line)
