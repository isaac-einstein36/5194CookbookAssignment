import cv2
from imutils import resize
import time

# Use cv2.VideoCapture instead of VideoStream
cap = cv2.VideoCapture(0)

# Allow time for the camera to warm up
time.sleep(2)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, img = cap.read()

    # ? Frame validation check
    if not ret or img is None:
        print("Failed to read frame. Skipping...")
        continue

    try:
        # Resize and process the frame
        img = resize(img, width=800)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.blur(img_gray, (3, 3))

        # Detect circles
        detected_circles = cv2.HoughCircles(
            img_blur, cv2.HOUGH_GRADIENT, 1, 20,
            param1=50, param2=30, minRadius=15, maxRadius=100
        )

        if detected_circles is not None:
            print(detected_circles)

            for pt in detected_circles[0]:
                a, b, r = pt[0], pt[1], pt[2]
                print(f"Circle at: ({a}, {b}) with radius {r}")
                cv2.circle(img, (int(a), int(b)), int(r), (0, 255, 0), 2)

        # Display the image
        cv2.imshow('Detected Circles', img)

        # Press 'x' to exit
        key = cv2.waitKey(1)
        if key == ord('x'):
            break

    except Exception as e:
        print(f"Error: {e}")

# Clean up
cap.release()
cv2.destroyAllWindows()
