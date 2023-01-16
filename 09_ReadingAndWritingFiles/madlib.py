import re
from pathlib import Path


# user_file = open('sample.txt', 'w')
# user_file.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
# user_file.close()

path_input = input("Enter destination of folder/ path along without filename: \n")
file_input = input("Enter name of file: \n")
user_file = open(Path(path_input)/file_input, 'r')
text = user_file.read()
print()
print(text)


sample =  re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

user = sample.findall(text)

for i in range(len(user)):
    if user[i] == 'ADJECTIVE':
        x = input(f"Enter {user[i].lower()}:")
        text = text.replace('ADJECTIVE',x,1)
    if user[i] == 'NOUN':
        x = input(f"Enter {user[i].lower()}: ")
        text = text.replace('NOUN', x,1)
    if user[i] == 'VERB':
        x = input(f"Enter {user[i].lower()}: ")
        text = text.replace('VERB',x,1)
    if user[i] == 'ADVERB':
        x = input(f"Enter {user[i].lower()}: ")
        text = text.replace('ADVERB',x,1)
output_file = open('sample.txt','w')
output_file.write(text)
output_file.close()
output_file = open('sample.txt','r')
replaced = output_file.read()

output_file.close()
print()
print(replaced)
