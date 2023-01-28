import ezgmail
import random

emailDict = {'sharan' : 'sharanv021104@gmail.com', 'svcodin' : 'svcodin22@gmail.com', 'shrisharanyan': 'shrisharanyan.clg@gmail.com'}

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
