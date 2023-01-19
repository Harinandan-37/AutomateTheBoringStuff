#we assume the files are numbered properly
import os
import re
import shutil

user_folder = input("Enter directory: ")
while True:
    if not os.path.exists(user_folder):
        print("No such directory exists! ")
        user_folder = input("Enter directory again: ")
    else:
        break
file_list = os.listdir(user_folder)
    

pattern = re.compile(r'^(.*?)(\d+)(.*?)$')



file_name = []

insertion = input("After which file do you want to insert file to? ")
while True:
    if insertion not in file_list:
        print("No such file!")
        insertion = input("After which file do you want to insert file to? ")
    else:
        break
while True:
    try:
        num_insert = int(input("No.of files that you want to insert: "))
        while True:
            if not num_insert > 0:
                num_insert = int(input("No.of files that you want to insert: "))
            else:
                break
        break
    except ValueError:
        pass

file_match = pattern.search(insertion)
num_last = int(file_match.group(2))
for folderName, subFolders, filenames in os.walk(user_folder):
    filenames.sort()
    for filename in filenames:
        filename = os.path.join(folderName, filename)
        name = os.path.basename(filename)
        match = pattern.search(name)
        if match is not None:
            file_name.append(name)
            before = match.group(1)
            number = int(match.group(2))
            after = match.group(3)

print(file_name)

#inserting file 

for folderName, subFolders, filenames in os.walk(user_folder):


    for i in range(len(file_name), num_last, -1):

        file1 = before + str(i) + after
        match_new = pattern.search(file1)
        number = int(match_new.group(2))
        num = number + num_insert
        # this task is to be done in a SINGLE folder only and not a folder tree. So this should suffice.
        new_file = user_folder + '/' + before + str(num) + after
        now_file = user_folder + '/' + file_name[i-1]
        print("before: " + now_file)
        print("renamed: " + new_file)
        shutil.move(now_file, new_file)
    break