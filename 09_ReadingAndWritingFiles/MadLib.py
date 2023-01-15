sampleFile = open('Sample.txt','r')

wordList = list(sampleFile.readlines())

capList = ['ADJECTIVE','NOUN','ADVERB','VERB']

checkList = []

prompt = []

count = 0

if 'ADJECTIVE' in wordList:
    checkList.append("Adjective")
    count += wordList.count('ADJECTIVE')
if 'NOUN' in wordList:
    checkList.append("Noun")
    count += wordList.count('NOUN')
if 'ADVERB' in wordList:
    count += wordList.count('ADVERB')
    checkList.append("Adverb")
if 'VERB' in wordList:
    count += wordList.count('VERB')
    checkList.append("Verb")

for i in range(count):
    prompt.append(input(f"Enter an {checkList[i]}: \n"))

sampleFile.close()

resultFile = open('Result.txt', 'a')
for i in range(len(wordList)):
    resultFile.write(
    wordList[i].replace(f'{capList[0]}', prompt[0])
    )
    resultFile.write(
    wordList[i].replace(f'{capList[1]}', prompt[1])
    )
    resultFile.write(
    wordList[i].replace(f'{capList[2]}', prompt[2])
    )
    resultFile.write(
    wordList[i].replace(f'{capList[3]}', prompt[3])
    )

    



