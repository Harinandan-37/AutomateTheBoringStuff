import re
def isStrong(pwd):
    try:
            pattern = re.compile(r'[0-9]?([a-z]+[A-Z]+[0-9]+|[a-z]+[0-9]+[A-Z]+|[A-Z]+[a-z]+[0-9]+|[A-Z]+[0-9]+[a-z]+|[0-9]+[A-Z]+[a-z]+|[0-9]+[a-z]+[A-Z])[0-9]?')
            sample = pattern.findall(pwd)
            print("It is Strong Password!!")
            print(sample)     

    except:
        print("""
        Password should be atleast 8 characters long
        It should contain both lower case and uppercase letters
        It should have atleast one numerical digit
        """)

while True:
    pwd = input("Enter a strong password: ")
    if len(pwd) < 8:

        print("""
    Password should be atleast 8 characters long
    It should contain both lower case and uppercase letters
    It should have atleast one numerical digit
                """)
        break
    isStrong(pwd)
