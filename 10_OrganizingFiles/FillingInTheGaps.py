#wrong
import os
import re
import shutil
user_folder = input("Enter directory: ")

pattern = re.compile(r'^(.*?)(\d+)(.*?)$')

file_num = []


for folderName, subFolders, filenames in os.walk(user_folder):
    for filename in filenames:
        sample = pattern.search(filename)
        num = int(sample.group(2))
        file_num.append(num)
        another_num.append(num)

file_num.sort()
print(file_num)
length = len(file_num)
for i in range(1,length):
    diff = int(file_num[i]) - int(file_num[i-1])
    if diff != 1:
        file_num[i] = int(file_num[i-1]) + 1
    else:
        continue

print(file_num)


for folderName, subFolders, filenames in os.walk(user_folder):
    for filename in filenames:

        sample = pattern.search(filename)
        before = sample.group(1)
        num = sample.group(2)
        after = sample.group(3)
        current_path = user_folder + '/' + filename

        new_path = user_folder + '/' + before + str(file_num[i]) + after
        # shutil.move(current_path, new_path)
        
        print("originally: " + current_path)
        print("renamed to: " + new_path)
        print()
