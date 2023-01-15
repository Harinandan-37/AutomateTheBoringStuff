#need to finish
import re
x = '        hello world         '

for i in range(len(x)):
    if x[i]==' ':
        continue
    elif x[i] != ' ':
        lindex = i
        break
for i in range(len(x)-lindex-1):
    if x[i+lindex] == ' ':
        continue
    

