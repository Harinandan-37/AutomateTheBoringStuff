import re
try:
    date = input("Enter a date: ")
    pattern = re.compile(r'^(3[01]|[1-2][0-9]|0[1-9])/(1[0-2]|0[1-9])/(0{3}[1-9]|0{2}[1-9]{2}|[0-1]{2}[1-9]{2}|2[0-9]{3})$')

    sample = pattern.search(date)

    day = int(sample.group(1))
    month = int(sample.group(2))
    year = int(sample.group(3))
    
    print()

    if month == 2:
        if year%4==0 or year%400==0:
            if day>29:
                print("Invalid <dd> for February ")
        else:
            if day > 28:
                print("Invalid <dd> for February")
            

    if day > 31:
        print("Invalid <dd> ")

    if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            print("Invalid <dd> for given month.")

    print()

    for i in range(len(sample[0])):
        print(sample[0][i], end = '')
        
    print()

except AttributeError:
    print("Enter an appropriate date in format <dd/mm/yyyy>")