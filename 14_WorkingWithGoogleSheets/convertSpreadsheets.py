import ezsheets
import os
import shutil

folderName = input("Enter folder directory of file: \n")
print()
fileName = input("Enter filename: \n")

ss = ezsheets.upload(os.path.join(folderName,fileName))
print()

formatOpt = int(input("Convert format - 1:CSV 2:Excel 3:HTML 4:ODS 5:PDF 6:TSV \nEnter your choice: "))
                
rawFileName = fileName.strip('.xlsx')
if formatOpt == 1:
    shutil.move(ss.downloadAsCSV(),(os.path.join(folderName,rawFileName) + '.csv'))

elif formatOpt == 2: 
    shutil.move(ss.downloadAsExcel(),(os.path.join(folderName,rawFileName) + '.xlsx'))

elif formatOpt == 3:
    shutil.move(ss.downloadAsHTML(),(os.path.join(folderName,rawFileName) + '.zip'))
    
elif formatOpt == 4:
    shutil.move(ss.downloadAsODS(),(os.path.join(folderName,rawFileName) + '.ods'))
    
elif formatOpt == 5:
    shutil.move(ss.downloadAsPDF(),(os.path.join(folderName,rawFileName) + '.pdf'))

elif formatOpt == 6:
    shutil.move(ss.downloadAsTSV(),(os.path.join(folderName,rawFileName) + '.tsv'))
