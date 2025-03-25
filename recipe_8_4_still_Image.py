from picamera2 import Picamera2
import cv2
import numpy as np  # Import numpy

# Initialize picamera2
picam2 = Picamera2()
picam2.start()

# Capture an image
img = picam2.capture_array()

# Stop the camera
picam2.stop()

# Load the image
#img = cv2.imread('coins.jpg')

# Resize the image
img = cv2.resize(img, (800, 600))

# Convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a blur to the image
img = cv2.blur(img, (3, 3))

# Detect circles in the image
detected_circles = cv2.HoughCircles(img,  
    cv2.HOUGH_GRADIENT, 1, 20, param1=50, 
    param2=60, minRadius=15, maxRadius=100)

print(detected_circles)

# Draw circles on the image
if detected_circles is not None:
    for pt in detected_circles[0]: 
        a, b, r = pt[0], pt[1], pt[2] 
        print(a, b)
        cv2.circle(img, (int(a), int(b)), int(r), (0, 0, 0), 2) 

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
