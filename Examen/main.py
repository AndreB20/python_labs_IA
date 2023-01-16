import cv2
import mediapipe as mp
import pyautogui
import time

from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.keyboard import Key

cap = cv2.VideoCapture(0)
mouse = mouse.Controller()
keyboard = keyboard.Controller()


hand_detector = mp.solutions.hands.Hands(min_detection_confidence= 0.5, min_tracking_confidence= 0.5)
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
index_y = 0

while cap.isOpened():
    start = time.time()

    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_height, frame_width, _ = frame.shape

    frame.flags.writeable = False

    output = hand_detector.process(rgb_frame)

    frame.flags.writeable = True

    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                if id == 4:
                    thumb_x = screen_width/frame_width * x
                    thumb_y = screen_height/frame_height * y

                if id == 8:#right click
                    index_x = screen_width/frame_width * x
                    index_y = screen_height/frame_height * y
                    if abs(thumb_x - index_x) < 40 and abs(thumb_y - index_y) < 40:
                        mouse.click(Button.right, 1)
                        pyautogui.sleep(0.2)
                    elif abs(thumb_y - index_y) < 400:
                        mouse.position = (thumb_x * 1.5, thumb_y * 1.5)

                if id == 17:#left click
                    pod_x = screen_width/frame_width * x
                    pod_y = screen_height/frame_height * y
                    if abs(thumb_x - pod_x) < 40 and abs(thumb_y - pod_y) < 40:
                        mouse.click(Button.left, 1)
                        pyautogui.sleep(0.2)
                    elif abs(thumb_y - pod_y) < 400:
                        mouse.position = (thumb_x * 1.5, thumb_y * 1.5)
#finger keyboard:
                if id == 12:        #W
                    middle_x = screen_width/frame_width * x
                    middle_y = screen_height/frame_height * y
                    print(abs(thumb_x - middle_x))
                    if abs(thumb_x - middle_x) < 40 and abs(thumb_y - middle_y) < 40:
                        keyboard.press('w')
                        pyautogui.sleep(0.1)
                        keyboard.release('w')
                        print("w")
                    elif abs(thumb_y - middle_y) < 400:
                        mouse.position = (thumb_x * 1.5, thumb_y * 1.5)

                if id == 16:        #R kon
                    ring_x = screen_width/frame_width * x
                    ring_y = screen_height/frame_height * y
                    if abs(thumb_x - ring_x) < 40 and abs(thumb_y - ring_y) < 40:
                        keyboard.press('r')
                        pyautogui.sleep(0.1)
                        keyboard.release('r')
                        print("r")
                    elif abs(thumb_y - ring_y) < 400:
                        mouse.position = (thumb_x * 1.5, thumb_y * 1.5)

                if id == 20:        #E
                    small_x = screen_width/frame_width * x
                    small_y = screen_height/frame_height * y
                    if abs(thumb_x - small_x) < 40 and abs(thumb_y - small_y) < 40:
                        keyboard.press('e')
                        pyautogui.sleep(0.1)
                        keyboard.release('e')
                        print("e")
                    elif abs(thumb_y - small_y) < 400:
                        mouse.position = (thumb_x * 1.5, thumb_y * 1.5)
    end = time.time()
    timeTotal = end - start
    fps = 1/timeTotal
    cv2.putText(frame, f'FPS: {int(fps)}', (20,50),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)


    cv2.imshow('ferestruta', frame)
    cv2.waitKey(1)
    #if cv2.waitKey(10) & 0xFF == ord('q'):
        #break