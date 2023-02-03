import ezgmail
import random


emailDict = {'sharan' : 'sharanv021104@gmail.com', 'svcodin' : 'svcodin22@gmail.com', 'shrisharanyan': 'shrisharanyan.clg@gmail.com'}
# I CAN ALSO READ A FILE CONTAINING THE NAMES AND EMAILS.
# I WOULD USE THE .readlines() TO GET A LIST OF ALL THE LINES.
# I WOULD THEN DIFFERENTIATE THE NAME AND EMAIL BY REGEX. I COULD DEFINE A REGULAR EXPRESSION THAT A GENERAL EMAIL WOULD HAVE.

nameList = ['sharan','svcodin','shrisharanyan']

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

choreDict = {}

for i in range(len(nameList)):
    ranChore = random.choice(chores)
    choreDict[nameList[i]] = ranChore
    chores.remove(ranChore)

print(choreDict)

for name, chore in choreDict.items():
    ezgmail.send(emailDict[name], 'Chore of the Day!', f'You have been assigned the "{chore}" chore! Work hard and finish it!')
