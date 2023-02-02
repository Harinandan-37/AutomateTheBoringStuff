import pyautogui
import pyperclip

window = pyautogui.getWindowsWithTitle('Notepad')

window[0].activate()

left = window[0].left
top = window[0].top


#print(left)
#print(top)


pyautogui.click(left+200,top+200)

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

text=pyperclip.paste()
print(text)
