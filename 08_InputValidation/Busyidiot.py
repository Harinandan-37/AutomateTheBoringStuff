import pyinputplus as pinp

while True:
    prompt = pinp.inputYesNo("Do you want to know how to keep an idiot busy? y/n\n")
    if prompt.lower() == 'no' or prompt.lower() == 'n':
        print('Thank you. Have a busy day.')
        break

