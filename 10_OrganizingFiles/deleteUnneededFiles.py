import os

user_path = input("Enter absolute directory to search: \n")
user_input = user_path
print()
if not os.path.exists(user_input):
    print("Path doesn't exist")

else: 
    for folderName, subFolders, filenames in os.walk(user_input):
        for filename in filenames:
            user_input = os.path.join(folderName,filename)
            if os.path.exists(user_input):
                size = os.path.getsize(user_input)
                if size > 100000000:
                    print(user_input,end=' ')
                    print(size)


    