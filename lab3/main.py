import keyboard
import pyautogui
import numpy as np
import cv2
import time

import win32api, win32con

#So to know how to use this BOT press the "start_button" ('z' in this case) on Top-Left corner and Bottom-Right corner
#After setting the screen space click manually as fast as possible the "START" tile button, because I didn't set up the
#blue tile

#Other things: I commented where the code needs to be deleted or commented for a cross-platform.

#REMINDER: import win32api, win32con; def click(x, y)  can be commented and use_win32 = False made it !!
#also on the tap_tile function delete the click() function because it will be commented or deleted doesn't matter

#And it depends on the site the between_tap_delay it varies, because on some sites it will read the click as double

start_button = "z"

between_tap_delay = 0.2

dark = np.array([0, 0, 0])
dark_high = np.array([255, 255, 75])

threshold = 10

use_win32 = False

height_multiplier = 1.0


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


last_lane = None

def tap_tile(image):
    global coords, WIDTH, HEIGHT, keys, last_lane
    for temp in range(1, int(HEIGHT * height_multiplier), 5):
        for i in range(4):
            if i == last_lane: continue

            last_lane = i
            x = int(i * WIDTH / 4 + WIDTH / 8)
            y = HEIGHT - temp

            if image[y][x] > threshold:  # if white aka TRUE [255,255,255]
                if use_win32:
                    click(x + coords[0], y + coords[1])
                else:
                    pyautogui.click(x=x + coords[0], y=y + coords[1])

                return

#stanga sus
while True:
    if keyboard.is_pressed(start_button):
        mousePos1 = pyautogui.position()
        print(mousePos1)
        break

time.sleep(1)

#dreapta jos
while True:
    if keyboard.is_pressed(start_button):
        mousePos2 = pyautogui.position()
        print(mousePos2)
        break

WIDTH = mousePos2.x - mousePos1.x
HEIGHT = mousePos2.y - mousePos1.y

time.sleep(1)

coords = (mousePos1.x, mousePos1.y, mousePos2.x, mousePos2.y)

while True:
    if keyboard.is_pressed(start_button):   #press again for stopping the game
        break

    image = np.array(pyautogui.screenshot(region=(mousePos1.x, mousePos1.y, WIDTH, HEIGHT)))
    image = cv2.inRange(image, dark, dark_high)

    tap_tile(image)
    time.sleep(between_tap_delay)

    # cv2.imshow("normal", scrot) #for seeing the HSV mode image from a screenshot
    # cv2.waitKey(0)
