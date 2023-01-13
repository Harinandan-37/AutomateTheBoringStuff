import random

coinFlip = []
i=0

while i<=100:
    if random.randint(0,1) == 0:
        coinFlip.append('H')
    else:
        coinFlip.append('T')
    i += 1


print(coinFlip)
l = len(coinFlip)

count = 0

for i in range(0,l-5,5):
    if coinFlip[i] == coinFlip[i+1] == coinFlip[i+2] == coinFlip[i+3] == coinFlip[i+4] == coinFlip[i+5]:
        count += 1
        
print(count)
percentage = count/l * 100
print(percentage)
