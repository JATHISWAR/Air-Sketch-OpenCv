import cv2 as cv
import numpy as np

# To set the opencv camera with 3,4,10 being the parameters width,height and brightness respectively
frameHeight = 600
frameWidth = 800
contrast = 150
capture = cv.VideoCapture(0)
capture.set(3,frameWidth)
capture.set(4,frameHeight)
capture.set(10,contrast)

# The value got from colorpicker for the colours blue, green and orange.
colors = [[5,107,0,19,255,255], [57,76,0,100,255,255], [90,48,0,118,255,255]]
colorvalues = [[51,153,255], [0,255,0],[255,0,0]]

mypoints = []

def findColor(image,colors,colorvalues):
    imageHSV = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    count = 0
    newpoints =[]
#Masking with respect to that particular colour. Output will show white for that HSV colour range in camera vision
    for colour in colors:
        lower = np.array(colour[0:3])
        upper = np.array(colour[3:6])
        mask = cv.inRange(imageHSV,lower,upper)
        a, b = getContours(mask) #get the countour points of the masked image
        cv.circle(finalImage, (a, b), 15, colorvalues[count], cv.FILLED) #draw a small circle on the tip of the contour
        if a != 0 and b != 0:
            newpoints.append([a, b, count]) #append the new points as movement progresses
        count += 1 # if no contours found, move to the next colour.
    return newpoints

def getContours(image):
    # cv.findContours returns the contour points of the masked image. Hierarchy represents relationship of contours.
    contours,heirarchy = cv.findContours(image,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for contour in contours:
        area = cv.contourArea(contour) #area of the contour points
        peri = cv.arcLength(contour, True) #perimeter of the contour points
        approx = cv.approxPolyDP(contour, 0.02 * peri, True) #It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify
        x, y, w, h = cv.boundingRect(approx) # get the dimensions of the approximated contour rectangle
    return x + w // 2, y # x+w//2 to return the tip of the contour which is easy for AirSketch

def AirSketch(mypoints,colourvalues):
    for pts in mypoints:
        #draw circles as and when point values are got from mypoints and draw with that colour
        cv.circle(finalImage,(pts[0],pts[1]),10,colorvalues[pts[2]],cv.FILLED)




# main function

while True:
    isTrue,image = capture.read() #read the opencv camera
    finalImage = image.copy() # make a copy of it for final camera view
    newpoints = findColor(image,colors,colorvalues) # finding the colour value of the show object in camera
    if len(newpoints) != 0:
        for newpts in newpoints:
            mypoints.append(newpts) #append points of the contour tip as and when there is a movement in camera
    if len(mypoints) != 0:  # when new points are appended, air sketch is shown on those locations
        AirSketch(mypoints,colorvalues)

    cv.imshow("Air Sketch",finalImage)  # showing the air sketch to the user.
    if cv.waitKey(1) & 0xFF == ord('d'): #wait for key press and on press d quit camera window
        break
