import random, time
from inputimeout import inputimeout
numberOfQuestions = 10
correctAnswers = 0

try: 
    for questionNumber in range(numberOfQuestions):
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)

        for i in range(3):

            prompt = inputimeout(prompt = "#%s: %s x %s = ?\n" % (questionNumber+1, num1, num2), timeout=8)

            while True:
                if not prompt.isdecimal():
                    print(str(prompt) + ' is not allowed as response.')
                    prompt = input("#%s: %s x %s = ?\n" % (questionNumber+1, num1, num2))
                else:
                    break

            if int(prompt) == num1*num2:
                print("Correct!")
                correctAnswers += 1
                break
            
            else:
                print("Incorrect!")
            time.sleep(1)
    
    print("Total Score: %s / %s" % (correctAnswers, numberOfQuestions))
    if correctAnswers == numberOfQuestions:
        print("Congratulations!! You got a perfect score!!")

except Exception:
    prompt = 'Timeover!!'
    print(prompt)
    print("Total Score: %s / %s" % (correctAnswers, numberOfQuestions))
    print("Bye...")

except KeyboardInterrupt:
    print("Total Score: %s / %s" % (correctAnswers, numberOfQuestions))
    print("Bye...")


