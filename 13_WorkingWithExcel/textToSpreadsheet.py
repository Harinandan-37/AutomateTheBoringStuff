import openpyxl

num_files = int(input("Enter number of files to be opened: "))
file_list = []

for i in range(num_files):
    file_list.append(input("Enter textfile name/directory: "))


wb = openpyxl.Workbook()
sheet = wb.active

column = 0

for i in range(num_files):
    text_file = open(file_list[i],'r')
    sentence_list = text_file.readlines()
    l1 = len(sentence_list)
    row = 0
    column += 1
    for sentence in sentence_list:

        for letter in sentence:
            row += 1
            sheet.cell(row=row, column=column).value = letter


wb.save("Sentence_in_Column.xlsx")

# I know I'm not closing the file. I have yet to learn how to use the 'with' keyword. 
# I'll first learn that.