import pyautogui
import time
import os



pyautogui.hotkey('win')
time.sleep(2)

pyautogui.typewrite('run')

time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.typewrite('chrome')
time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.typewrite('https://jira.anthem.com/secure/Dashboard.jspa')
time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(7)
i=0
while i<10:
    pyautogui.hotkey('tab')
    i=i+1

path=os.path.dirname(__file__)
f = open(f"{path}\main.txt","r")


a=f.readline()

time.sleep(1)
pyautogui.typewrite(a)
time.sleep(1)
pyautogui.hotkey('enter')


