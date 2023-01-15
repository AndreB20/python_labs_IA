import cv2
import mediapipe as mp
import pyautogui
import time
from pynput.mouse import Button, Controller

cap = cv2.VideoCapture(0)
mouse = Controller()

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
                if id == 8:
                    #cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 0, 255))
                    index_x = screen_width/frame_width * x
                    index_y = screen_height/frame_height * y
                    print(index_x)
                    print(" ")
                    print(index_y)

                if id == 4:
                    #cv2.circle(img=frame, center=(x,y), radius=5, color=(0, 220, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    if abs(index_y - thumb_y) < 20:
                        mouse.click(Button.left, 1)
                        pyautogui.sleep(0.5)
                    elif abs(index_y - thumb_y) < 400:
                        mouse.position = (index_x, index_y)
    end = time.time()
    timeTotal = end - start
    fps = 1/timeTotal
    cv2.putText(frame, f'FPS: {int(fps)}', (20,50),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)


    cv2.imshow('ferestruta', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break