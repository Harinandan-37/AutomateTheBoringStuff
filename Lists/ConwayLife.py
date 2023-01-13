import random, copy, time

WIDTH = 60
HEIGHT = 20

#Getting first cell.
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
            
    nextCells.append(column)

#main program.  
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end = '')
        print()

        


    for x in range(WIDTH):
        for y in range(HEIGHT):
            #defining co-ordinates.
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            numNeighbours = 0
            if currentCells[left][above] == '#':
                numNeighbours += 1
            if currentCells[x][above] == '#':
                numNeighbours += 1
            if currentCells[right][above] == '#':
                numNeighbours += 1
            if currentCells[left][y] == '#':
                numNeighbours += 1
            if currentCells[right][y] == '#':
                numNeighbours += 1
            if currentCells[left][below] == '#':
                numNeighbours += 1
            if currentCells[x][below] == '#':
                numNeighbours += 1
            if currentCells[right][below] == '#':
                numNeighbours += 1

            #modify next cell based on rules.
            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = '#' #living cell has 2 or 3 neighbours
            elif currentCells[x][y] == ' ' and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = '#' #dead cell has 2 or 3 neighbours
            else:
                nextCells[x][y] = ' ' #if any cell doesn't have enough neighbours.
             
    time.sleep(0.1) #pause before every cell is printed.
        
        
    
        
    
