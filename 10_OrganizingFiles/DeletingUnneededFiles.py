#sooo wrongg!!
import os


user_folder = input("Enter directory to search: ")


os.chdir(user_folder)

for folderName, subFolders, filenames in os.walk(user_folder):
    print(subFolders)
    print(filenames)
    for subFolder in subFolders:
        subFolder = os.path.join(user_folder,subFolder)
        if os.path.exists(subFolder):
            subFolder_size = os.path.getsize(subFolder)
        if os.path.exists(subFolder) and int(subFolder_size) > 1:
            print(subFolder)
        for filename in filenames:
            filename = os.path.join(subFolder,filename)
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
            if os.path.exists(filename) and int(file_size) > 1:
                print(filename)
                
    for filename in filenames:
        filename = os.path.join(user_folder,filename)
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
        if os.path.exists(filename) and int(file_size) > 1:
            print(filename)





















# if int(subFolder_size) > 1:
        #     print(subFolder)
        #     subFolder = os.path.basename(subFolder)
        #     for filename in filenames:
        #         filename = os.path.abspath(filename)
        #         file_size = os.path.getsize(filename)
        
        #         if int(file_size) > 1 :
        #             print(filename)
        #             filename = os.path.basename(filename)
        