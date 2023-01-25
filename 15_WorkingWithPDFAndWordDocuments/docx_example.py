import docx
import os
import readDocx
path = os.getcwd()
path = os.path.join(path,'automate_online-materials')

doc = docx.Document(os.path.join(path,'demo.docx'))

l = len(doc.paragraphs)
print(readDocx.getText(os.path.join(path,'demo.docx')))