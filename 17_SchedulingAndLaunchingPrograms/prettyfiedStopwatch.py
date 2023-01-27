import time
import pyperclip

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl+C to quit.')

input()
print('Started.')

start = time.time()
lasttime = start

lapNum = 1
timeStamps = []
try:
    while True:
        #check for any input, not just enter. But this works as well.
        input()

        laptime = round(time.time() - lasttime, 2)
        totaltime = round(time.time() - start, 2)
        strlapnum = 'Lap #%s: ' % str(lapNum).rjust(3)
        strtotalTime = str(totaltime).rjust(7)
        strlapTime = ' (%s)' % str(laptime).rjust(5)

        toPrint = strlapnum + strtotalTime + strlapTime
        print(toPrint)
        lapNum += 1
        lasttime = time.time()
        timeStamps.append(toPrint)

except KeyboardInterrupt:
    print()
    print('\nDone.')
timeStamps = '\n'.join(timeStamps)
print(timeStamps)
pyperclip.copy(timeStamps)
