import cv2
import numpy as np
from picamera2 import Picamera2
import time

# set Width and Height of output Screen
frameWidth = 640
frameHeight = 480

# Initialize picamera2
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (frameWidth, frameHeight)})
picam2.configure(config)
picam2.start()

# object color values (HSV ranges)
myColors = [
    [5, 107, 0, 19, 255, 255],  # Adjust these values to match your pointer
    [133, 56, 0, 159, 156, 255],
    [57, 76, 0, 100, 255, 255],
    [90, 48, 0, 118, 255, 255]
]

# color values which will be used to paint (BGR)
myColorValues = [
    [51, 153, 255],  # orange
    [255, 0, 255],   # purple
    [0, 255, 0],     # green
    [255, 0, 0]      # blue
]

# [x , y , colorId]
myPoints = []

# Function to pick color of object
def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)

        # Apply morphological transformations (optional)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=1)

        x, y = getContours(mask)

        # Draw circles
        cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints

# Contours function used to improve accuracy of paint
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:  # Adjust threshold
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

# Function to draw on canvas (draws the tracked points on the result image)
def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

# Smoothing variables
smoothening = 10  # The higher the number, the smoother it will be
previous_x, previous_y = 0, 0

# running infinite while loop so that
while True:
    img = picam2.capture_array()
    imgResult = img.copy()

    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

            # Smooth the movement
            x, y = newP[0], newP[1]
            x = previous_x + (x - previous_x) / smoothening
            y = previous_y + (y - previous_y) / smoothening

            previous_x, previous_y = x, y

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
