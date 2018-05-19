import numpy as np
import cv2 as cv
curCamera = 1 #Номер камеры для работы. Любая доступная "-1", Первая - "0", вторая - "1"

def grayer(frame):
    image = frame
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (3, 3), 0)
    #edged = cv.Canny(gray, 10, 250)

    return gray

def gradientor(frame):
    gradX = cv.Sobel(grayer(frame), ddepth=cv.cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv.Sobel(grayer(frame), ddepth=cv.cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # subtract the y-gradient from the x-gradient
    gradient = cv.subtract(gradX, gradY)
    gradient = cv.convertScaleAbs(gradient)
    blurred = cv.blur(gradient, (9, 9))
    (_, thresh) = cv.threshold(blurred, 225, 255, cv.THRESH_BINARY)

    return gradient

cap = cv.VideoCapture(curCamera)

StopThisFrame = False
while(True):
    if not StopThisFrame:
       _, frame = cap.read()
       print(frame)
   #ff = grayer(frame)
    cv.imshow('I am watch you', frame)
    cv.imshow('Test', gradientor(frame))
    if cv.waitKey(1) & 0xFF == ord('p'):
        StopThisFrame = not StopThisFrame
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
