import os, shutil

user_dir = input("Enter directory: ")
user_ext = input("Enter file extension of the files you want to copy: ")
copy_dir = input("Enter directory of destination folder: ")
for folderName, subFolders, filenames in os.walk(user_dir):
    for filename in filenames:
        print(os.path.getsize(filename))
        print(filename)
        if filename.endswith(user_ext):
            shutil.copy(user_dir + '/' + f'{filename}', copy_dir)
        else:
            continue
files = os.listdir(copy_dir)
print(files)