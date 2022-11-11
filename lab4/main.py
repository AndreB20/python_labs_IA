import time
import pyautogui
import keyboard

def cautare_goagle():
    if pyautogui.locateOnScreen('schema.png', confidence=0.5)!=None:
        print("mere")
        camp_google=pyautogui.locateOnScreen('schema.png',confidence=0.5)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("https://youtube.com")
        pyautogui.press("enter")
        time.sleep(6)
        cautare_yt()
    else:
        print("teapa")

def cautare_yt():
    if pyautogui.locateOnScreen('yt_search.png', confidence = 0.7):
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

def abon():
    if pyautogui.locateOnScreen('zonait.png', confidence=0.7):
        print("ne abonam")
        camp_zonait = pyautogui.locateOnScreen('abon.png', confidence = 0.7)
        pyautogui.click(camp_zonait)
        time.sleep(3)
        cautare_zonait()
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
        rulare_tab()
    else:
        print("BAAAAAA")

def rulare_tab():
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    n=13
    while True:
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(5)
        if pyautogui.locateOnScreen('okeh.png', confidence = 0.7):
            camp = pyautogui.locateOnScreen('okeh.png', confidence = 0.7)
            pyautogui.click(camp)
            time.sleep(1)
            camp = pyautogui.locateOnScreen('bieck.png',confidence = 0.7)
            pyautogui.click(camp)
        while True:
            for i in range(n):
                pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(3)
            n = n + 2
            if pyautogui.locateOnScreen('okeh.png', confidence=0.7):
                camp = pyautogui.locateOnScreen('okeh.png', confidence=0.7)
                pyautogui.click(camp)
                time.sleep(1)
                camp = pyautogui.locateOnScreen('bieck.png', confidence=0.7)
                pyautogui.click(camp)
                time.sleep(2)


time.sleep(2)
cautare_goagle()