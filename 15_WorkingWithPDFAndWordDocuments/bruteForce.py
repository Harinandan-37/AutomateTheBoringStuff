import PyPDF2 as pdf

filetext = open('/home/shrisharanyan/AutomateTheBoringStuff/15_WorkingWithPDFAndWordDocuments/pwdList.txt', 'r')
word_list = filetext.readlines()
pdfReader = pdf.PdfFileReader(open('/home/shrisharanyan/AutomateTheBoringStuff/15_WorkingWithPDFAndWordDocuments/automate_online-materials/encrypted.pdf','rb'))
for pwd in word_list:
    pwd = pwd.replace('\n','')
    result1 = pdfReader.decrypt(pwd.lower())
    print(pwd.lower())
    if result1 == 1:
        print()
        print("Password: " + pwd.lower())
        break
    result2 = pdfReader.decrypt(pwd.upper())
    print(pwd.upper())
    if result2 == 1:
        print()
        print("Password: " + pwd.upper())
        break
if result1 != 1 and result2 != 1:
    print("No Matches")
