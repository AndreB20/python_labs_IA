import cv2
import keyboard

face_cascade = cv2.CascadeClassifier('ceva.xml')
cap = cv2.VideoCapture(0)

while not keyboard.is_pressed('esc'):
    _,img = cap.read()
    gray = cv2.cvtColro(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Imagine:", img)
cv2.waitKey()