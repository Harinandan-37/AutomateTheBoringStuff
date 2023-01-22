import openpyxl

filename = input("Excel File Directory: ")

wb = openpyxl.load_workbook(filename)
sheet = wb.active

wb_new = openpyxl.Workbook()
sheet_new = wb_new.active
a = {}
a["row-1"] = {}
for row in range(1, sheet.max_row):
    for column in range(1, sheet.max_column):
        a["row-" + str(row)]["column-"+str(column)] = sheet.cell(row=row,column=column).value

for row in range(1,sheet.max_row):
    for column in range(1, sheet.max_column):
        sheet.cell(row=column,column=row).value = a["row-"+str(row)]["column-"+str(column)]


wb.save("Inverted.xlsx")
wb_new.save("Temporary.xlsx")