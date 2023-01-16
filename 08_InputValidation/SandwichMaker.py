import pyinputplus as pinp

breadTypeChoice = pinp.inputMenu(['wheat', 'white', 'sourdough'], prompt = "What type of bread do you want?\n")
proteinTypeChoice = pinp.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt = "What type of cheese do you want?\n")

cheeseChoice = pinp.inputYesNo("Do you want cheese?")

if cheeseChoice.lower() == 'yes':
    cheeseTypeChoice = pinp.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt = "What type of cheese do you want?\n")

mayoChoice = pinp.inputYesNo("Do you want Mayo?")
mustardChoice = pinp.inputYesNo("Do you want mustard?")
tomatoChoice = pinp.inputYesNo("Do you want tomato?")
lettuceChoice = pinp.inputYesNo("Do you want lettuce?")

breadPrice = 0
proteinPrice = 0
cheesePrice = 0
mayoPrice = 10
mustardPrice= 10
tomatoPrice = 7
lettucePrice = 3
prepFee = 200

number = pinp.inputInt("No. of sandwiches you want of this style: ", min = 1)

 
if breadTypeChoice == 'wheat':
    breadPrice += 30
elif breadTypeChoice == 'white':
    breadPrice += 40
elif breadTypeChoice == 'sourdough':
    breadPrice += 60

if proteinTypeChoice == 'chicken':
    proteinPrice += 40
elif proteinTypeChoice == 'turkey':
    proteinPrice += 60
elif proteinTypeChoice == 'ham':
    proteinPrice += 50
elif breadTypeChoice == 'tofu':
    proteinPrice += 30

if cheeseTypeChoice == 'cheddar':
    cheesePrice += 40
elif cheeseTypeChoice == 'Swiss':
    cheesePrice += 40
elif cheeseTypeChoice == 'mozarella':
    cheesePrice += 40

price = (prepFee + breadPrice + proteinPrice + cheesePrice + mayoPrice + mustardPrice + tomatoPrice + lettucePrice) * number

print("Price: %s" % price)