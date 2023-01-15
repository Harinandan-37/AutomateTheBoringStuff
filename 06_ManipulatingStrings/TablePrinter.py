tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
tableLength = len(tableData)
innerLength = len(tableData[0])
#finding the longest
longest = tableData[0][0]
for i in tableData:
    for j in i:
        if len(j) > len(longest):
            longest = j
#printing table
for j in range(innerLength):
    for i in range(tableLength):
        #adjusting using rjust.
        print(tableData[i][j].rjust(len(longest)), end = ' ')
    print()
