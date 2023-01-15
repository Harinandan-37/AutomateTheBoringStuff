import re
try:
    date = input("Enter a date: ")
    pattern = re.compile(r'^(3[01]|[1-2][0-9]|0[1-9])\/(1[0-2]|0[1-9])\/(0{3}[1-9]|0{2}[1-9]{2}|[0-1]{2}[1-9]{2}|2[0-9]{3})$')
    0
    sample = pattern.findall(date)
    for i in range(len(sample[0])):
        print(sample[0][i], end = ' ')
    print()
except:
    print("Enter an appropriate date in format <dd/mm/yyyy>")