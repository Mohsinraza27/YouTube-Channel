# pip install https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54

import pyautogui as pg
import time

time.sleep(10)
txt = open('animals.txt', 'r').readlines()

a = "Saben is a "
for i in txt:
    pg.write(a+i)
    pg.press('Enter..')