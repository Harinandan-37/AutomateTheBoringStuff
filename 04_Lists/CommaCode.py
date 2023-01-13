spam = ['apples', 'bananas', 'tofu', 'cats']
def sentenceList(lst):
    length = len(lst)
    for i in range(length):
        if i == 0:
            print(spam[i], end = '')
        elif i != (length-1):
            print(', ' + spam[i], end='')
        elif i == (length-1):
            print(' and ' + spam[i])
    if length == 0:
        print("Empty String!!")
        return 0
    return length
print(sentenceList(spam))
