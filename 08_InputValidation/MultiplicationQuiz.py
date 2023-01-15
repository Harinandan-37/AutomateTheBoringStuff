import pyinputplus as pinp
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber+1, num1, num2)

    try:
        pinp.inputStr(prompt, allowRegexes=['^%s$' % (num1*num2)],
                            blockRegexes=[('.*','Incorrect!')],
                            timeout=8,
                            limit=3)
    except pinp.TimeoutException:
        print("Out of time!!")
    except pinp.RetryLimitException:
        print('Out of tries!!')
    
    else:
        print('Correct!!')
        correctAnswers += 1
    time.sleep(1)
print('Score: %s / %s' % (correctAnswers,numberOfQuestions))