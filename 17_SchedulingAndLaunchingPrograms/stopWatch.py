import time

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl+C to quit.')

input()
print('Started.')

start = time.time()
lasttime = start

lapNum = 1

try:
    while True:
        #check for any input, not just enter. But this works as well.
        input()

        laptime = round(time.time() - lasttime, 2)
        totaltime = round(time.time() - start, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totaltime, laptime))
        lapNum += 1
        lasttime = time.time()
    
except KeyboardInterrupt:
    print('\nDone.')
