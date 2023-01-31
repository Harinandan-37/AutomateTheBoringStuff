import pyautogui as py
import pyperclip
import time

#I can't use the Window features since I'm using Linux.
#we  will manually open a window after we run the program.
time.sleep(10)
#we can also retrieve the target position by using py.position() in case of a text box etc.

py.click(960, 540) #to make window active

py.hotkey('ctrl','a')
py.hotkey('ctrl','c')
text = pyperclip.paste()

print(text)

