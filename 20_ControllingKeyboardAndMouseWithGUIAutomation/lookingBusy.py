import time
import pyautogui as pg

while True:
    time.sleep(10)
    pg.moveRel(1,0)
    pg.moveRel(-1,0)