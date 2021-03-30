import cv2 as cv
import numpy as np

# To set the opencv camera with 3,4,10 being the parameters width,height and brightness respectively
frameWidth = 640
frameHeight = 480
brightness = 150
capture = cv.VideoCapture(0)
capture.set(3, frameWidth)
capture.set(4, frameHeight)
capture.set(10,brightness)

def empty(a):
    pass

# creating a trackbar for HSV values
cv.namedWindow("HSV")
cv.resizeWindow("HSV",640,240)
cv.createTrackbar("HUE Min","HSV",0,179,empty)
cv.createTrackbar("SAT Min","HSV",0,255,empty)
cv.createTrackbar("VALUE Min","HSV",0,255,empty)
cv.createTrackbar("HUE Max","HSV",179,179,empty)
cv.createTrackbar("SAT Max","HSV",255,255,empty)
cv.createTrackbar("VALUE Max","HSV",255,255,empty)

while True:

    _, img = capture.read()
    imgHsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("HUE Min","HSV")
    h_max = cv.getTrackbarPos("HUE Max", "HSV")
    s_min = cv.getTrackbarPos("SAT Min", "HSV")
    s_max = cv.getTrackbarPos("SAT Max", "HSV")
    v_min = cv.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv.getTrackbarPos("VALUE Max", "HSV")
    myarr = np.array([h_min,h_max,s_min,s_max,v_min,v_max]) #get the HSV values as and when the trackbar moves
    print(myarr)  #print the values based on Trackbar Position


    lower = np.array([h_min,s_min,v_min]) #set the lower end of the HSV values
    upper = np.array([h_max,s_max,v_max]) #set the upper end of the HSV values
    mask = cv.inRange(imgHsv,lower,upper) #mask the image with the lower and upper HSV values set
    result = cv.bitwise_and(img,img, mask = mask)  #result is a combination of masked and original image

    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    flipped_img = cv.flip(img,1)
    flipped_mask= cv.flip(mask,1)
    flipped_result = cv.flip(result,1)
    hStack = np.hstack([flipped_img,flipped_mask,flipped_result]) #stack all the three images.
    cv.imshow('Color Value Finder',hStack) 
    if cv.waitKey(1) & 0xFF == ord('d'):#wait for key press and on press d quit camera window
        break

capture.release()
cv.destroyAllWindows()

