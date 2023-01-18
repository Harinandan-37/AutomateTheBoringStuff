#we assume the files are numbered properly
import os
import re
import shutil
user_folder = input("Enter directory: ")

pattern = re.compile(r'^(.*?)(\d+)(.*?)$')

# file_num = []


# for folderName, subFolders, filenames in os.walk(user_folder):
#     for filename in filenames:
#         sample = pattern.search(filename)
#         num = int(sample.group(2))
#         file_num.append(num)
        

# file_num.sort()

# print(file_num)

# length = len(file_num)
# for i in range(1,length):
#     diff = int(file_num[i]) - int(file_num[i-1])
#     if diff != 1:
#         file_num[i] = int(file_num[i-1]) + 1
#     else:
#         continue

# print(file_num)

# i = 0
# for folderName, subFolders, filenames in os.walk(user_folder):
#     filenames.sort()
#     for filename in filenames:

#         sample = pattern.search(filename)
#         before = sample.group(1)
#         num = sample.group(2)
#         after = sample.group(3)
#         current_path = user_folder + '/' + filename
#         new_path = user_folder + '/' + before + str(file_num[i]) + after
#         if new_path != current_path:
#             print("originally: " + current_path)
#             print("renamed to: " + new_path)
#             shutil.move(current_path, new_path)
#         i += 1
#         print()

#inserting file
insertion = input("After which file do you want to insert file to? ")
num_insert = int(input("No.of files that you want to insert: "))
match = pattern.search(insertion)
num_last = int(match.group(2))
for folderName, subFolders, filenames in os.walk(user_folder):
    filenames.sort()
    l = len(filenames)
    for filename in filenames:
        
        for i in range(num_last, l):
            current_path1 = user_folder + '/' + [i]
            before_file = match.group(1)
            num_file = match.group(2)
            after_file = match.group(3)

            new_path1 = user_folder + '/' + before_file + str(i+num_insert) + after_file
            if current_path1 != new_path1:
                print("originally: " + current_path1)
                print("renamed to: " + new_path1)
                print()


    
