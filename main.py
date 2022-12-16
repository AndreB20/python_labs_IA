import cv2
import keyboard as k
face_cascade = cv2.CascadeClassifier('ceva.xml')
img = cv2.imread('ching_ching.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

img = cv2.resize(img, (600,400))
cv2.imshow("Imagine:", img)
cv2.waitKey()
