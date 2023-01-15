import random, time
import pyinputplus as pinp
numberOfQuestions = 10
correctAnswers = 0

try: 
    for questionNumber in range(numberOfQuestions):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

        for i in range(3):

            prompt = input(timeout = 8, limit = 3)
            while True:
                if not prompt.isdecimal():
                    prompt = input("#%s: %s x %s = ?\n" % (questionNumber, num1, num2), timeout = 8, limit = 3)
                else:
                    break

                print(str(prompt) + ' is not allowed as response.')
                
            if prompt == num1*num2:
                print("Correct!")
                correctAnswers += 1
                break
            
            else:
                print("Incorrect!")
            time.sleep(1)

    print("Total Score: %s / %s" % (correctAnswers, numberOfQuestions))

except pinp.TimeoutException:
    print('Out of time!')

except pinp.RetryLimitException:
    print('Out of tries!')
