import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

sheet = ss[0]
columnOne = sheet.getColumn(1)
max_row = 0
for i, value in enumerate(columnOne):
    if value != '':
        max_row += 1
    else:
        continue

for rowNum in range(2, max_row):

    evaluate = (int(sheet.getRow(rowNum)[0]) * int(sheet.getRow(rowNum)[1]) == int(sheet.getRow(rowNum)[2]))
    if evaluate:
        continue
    else:
        wrongRowNum = rowNum

wrongRow = sheet.getRow(wrongRowNum)

print("The wrong row is Row Number %s : %s, %s, %s" % (wrongRowNum, wrongRow[0], wrongRow[1], wrongRow[2]))

