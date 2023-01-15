import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')

guess = ''
tupl = ('heads', 'tails')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug("toss = " + str(toss) + " and guess = " + str(guess))
if tupl[0] == guess.lower():
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()

    logging.debug("toss = " + str(toss) + "and guesss = " + str(guess))
    if tupl[toss] == guesss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')