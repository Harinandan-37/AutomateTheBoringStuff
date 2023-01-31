import pyautogui, time
time.sleep(5)

pyautogui.click()

distance = 400
change = 10
pyautogui.click(682,415)
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2) #move right
    distance -= change
    pyautogui.drag(0, distance, duration=0.2) #move down
    pyautogui.drag(-distance, 0, duration=0.2) #move left
    distance -= change
    pyautogui.drag(0, -distance, duration=0.2) #move up