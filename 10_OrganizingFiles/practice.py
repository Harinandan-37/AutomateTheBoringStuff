import os
import zipfile
from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'chall.zip')
exampleZip.extractall()
exampleZip.close()





# for folderName, subFolders, fileNames in os.walk('/home/shrisharanyan/AutomateTheBoringStuff1/Dictionary'):
#     print()
#     print("The current folder name is " + folderName)

#     for subFolder in subFolders:
#         print("Subfolder of " + folderName + ":" + subFolder)
    
#     for fileName in fileNames:
#         print("File inside " + folderName + ":" + fileName)

#     print('')