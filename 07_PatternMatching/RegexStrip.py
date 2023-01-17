#need to finish
import re

def strip(user_input, c=""):
    if c == "":
        pattern = re.compile(r'^\s+|\s+$') #we check input endswith or/and starts with space or tab etc.
        new_strip = pattern.sub("",user_input)
    else:
        no_space = strip(user_input, "") #we need to first remove any spaces before removing the character.
        pattern = re.compile(rf'^{c}+|{c}+$')#we check input endswith or/and starts with given string.
        new_strip = pattern.sub("", no_space)
    
    return new_strip
print()
string = input("input string to be stripped: ")
strip_char = input("character do you want to strip: ")

print(strip(string,strip_char))


