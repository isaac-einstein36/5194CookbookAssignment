import cv2
import numpy as np
from picamera2 import Picamera2
import time

# Initialize Picamera2
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (1280, 720)}))
picam2.start()

# Allow camera to warm up
time.sleep(2)

while True:
    # Capture an image frame
    img = picam2.capture_array()

    # Resize to 800px width while maintaining aspect ratio
    height, width = img.shape[:2]
    new_width = 800
    new_height = int((new_width / width) * height)
    img = cv2.resize(img, (new_width, new_height))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # **Enhance image quality for better detection**
    gray = cv2.GaussianBlur(gray, (9, 9), 2)  # Reduce noise with strong blur
    gray = cv2.medianBlur(gray, 5)  # Median blur to remove small artifacts

    # **Apply Adaptive Thresholding to Remove Background Noise**
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 3)

    # **Detect circles using refined parameters**
    detected_circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1.2, 30,
                                        param1=70, param2=30, minRadius=20, maxRadius=150)

    # Draw detected circles
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            cv2.circle(img, (a, b), r, (0, 255, 0), 3)  # Green circles

    # Show thresholded image and detected circles
    cv2.imshow('Thresholded', thresh)
    cv2.imshow('Detected Circles', img)

    # Press 'x' to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('x'):
        break

# Cleanup
cv2.destroyAllWindows()
picam2.close()
