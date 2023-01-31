import pyautogui as py
import time
import sys
while 1:
    try:
        recipient = input('Recipient username: ')
        text = input("Enter message: ")


        searchBar = py.locateOnScreen('chat_searchbar.png')


        searchSpace = (searchBar.left + 70, searchBar.top + 20)
        time.sleep(3)
        py.click(searchSpace)


        py.write(recipient)


        if py.locateOnScreen('chat_noResult.png') is not None:
            print("No Search Results!")
            py.hotkey('ctrl','a'); py.write(['backspace'])
            continue

        time.sleep(3)

        py.write(['down','enter'])

        time.sleep(2)

        py.write(text); py.write(['enter'])

    except AttributeError:
        print("Open the chat site or refresh it!!")
    except KeyboardInterrupt:
        print("\n\nBye...")
        sys.exit()