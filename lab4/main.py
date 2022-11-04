import time

import pyautogui
import keyboard

def cautare_goagle():
    if pyautogui.locateOnScreen('schema.png', confidence=0.7)!=None:
        print("mere")
        camp_google=pyautogui.locateOnScreen('schema.png',confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("https://youtube.com")
        pyautogui.press("enter")
        time.sleep(6)
        cautare_yt()
    else:
        print("teapa")

def cautare_yt():
    if pyautogui.locateCenterOnScreen('yt_search.png', confidence = 0.7):
        print("SUNTEM PE YT")
        camp_yt = pyautogui.locateOnScreen('yt_search.png', confidence = 0.7)
        pyautogui.click(camp_yt)
        time.sleep(3)
        pyautogui.write("zona it")
        pyautogui.press("enter")
        time.sleep(8)
        cautare_abon()
    else:
        print("iar ti ai luat teapa :(((")

def cautare_abon():
    if pyautogui.locateOnScreen('abon.png', confidence = 0.7):
        print("SUNTEM PE ZONA")
        camp_abon = pyautogui.locateOnScreen('abon.png', confidence = 0.7)
        pyautogui.click(camp_abon)
        time.sleep(3)
    else:
        print("BAAAAAA")
time.sleep(2)
cautare_goagle()
