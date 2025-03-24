import cv2
import numpy as np
from picamera2 import Picamera2
from time import sleep
from datetime import datetime  # Import datetime module

diff_threshold = 10000000  # Adjusted the threshold to reduce sensitivity

# Initialize the Picamera2 object
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()

def getImage():
    # Capture a frame from the camera
    im = picam2.capture_array()
    
    # Convert to grayscale
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    # Apply a blur to smooth the image
    im = cv2.blur(im, (20, 20))
    
    return im

# Get the initial image
old_image = getImage()

while True:
    # Get the new image
    new_image = getImage()
    
    # Compute the absolute difference between the old and new image
    diff = cv2.absdiff(old_image, new_image)
    
    # Sum the pixel differences to get a 'movement score'
    diff_score = np.sum(diff)
    
    # If the movement score exceeds the threshold, print the timestamp and message
    if diff_score > diff_threshold:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current timestamp
        print(f"Movement detected at {timestamp}")
    
    # Update the old image with the new one for the next iteration
    old_image = new_image

    # Optional: Sleep for a small amount of time to avoid overwhelming the CPU
    sleep(0.1)
