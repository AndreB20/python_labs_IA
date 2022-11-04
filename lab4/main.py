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
        cautare_zonait()
    else:
        print("iar ti ai luat teapa :(((")

def cautare_zonait():
    if pyautogui.locateOnScreen('zonait.png', confidence = 0.7):
        print("SUNTEM PE ZONA")
        camp_zonait = pyautogui.locateOnScreen('zonait.png', confidence = 0.7)
        pyautogui.click(camp_zonait)
        time.sleep(3)
        cautare_tab()
    else:
        print("BAAAAAA")

def cautare_tab():
    if pyautogui.locateOnScreen('videoclipuri.png', confidence = 0.7):
        print("SUNTEM PE ZONA")
        camp_zonait = pyautogui.locateOnScreen('videoclipuri.png', confidence = 0.7)
        pyautogui.click(camp_zonait)
        time.sleep(3)
    else:
        print("BAAAAAA")

time.sleep(2)
cautare_goagle()
