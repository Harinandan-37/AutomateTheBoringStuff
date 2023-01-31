import time, pyautogui

while True:
    time.sleep(10)
    x,y = pyautogui.position()
    pyautogui.moveTo(x+1,y)
    pyautogui.moveTo(x-1,y)
    
