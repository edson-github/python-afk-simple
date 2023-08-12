import pyautogui as pg
import random
import time

while True:
    x = random.randint(400, 600)
    y = random.randint(600, 800)
    pg.moveTo(x, y, 0.5)
    time.sleep(random.randint() * 2)
