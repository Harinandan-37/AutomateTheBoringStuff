import ezsheets

# https://docs.google.com/forms/d/1V2Jq8aT63RGgntxp0-BRbA3soKalpw5xwV9crp3Uxs0/edit#responses

ss = ezsheets.Spreadsheet('155zOjZ22TjETSo3u6RXXykJwc5eCnbIWpq4yWPzE11g')

ss.refresh()

sheet = ss[0]

responseDict = {}

columnOne = sheet.getColumn(1)
max_row = 0
for i, value in enumerate(columnOne):
    if value != '':
        max_row += 1
    else:
        continue

# rowOne = sheet.getRow(1)
# max_column = 0
# for i, value in enumerate(rowOne):
#     if value != '':
#         max_column += 1
#     else:
#         continue


for row in range(2,max_row + 1):
    responseDict[sheet.getRow(row)[1]] = sheet.getRow(row)[2]

print(responseDict)