from picamera2 import Picamera2
import cv2
import time

# Initialize the camera
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640,480)})
picam2.configure(config)

# Start the camera
picam2.start()
time.sleep(2)

# capture the image
img = picam2.capture_array()

# display the image with OpenCV
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows

print("Code Finished Running")

# Stop the camera
picam2.stop()
