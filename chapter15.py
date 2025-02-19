"""
5194 Homework 8
Isaac Einstein

Chapter 15 Cookbook Assignment:
Recipe 15.1, Using a Four-Digit LED Display

Problem Statement:
You want to display a four-digit number in an old-fashioned, seven-segment LED display.
"""

## Code to install required adafruit libraries
# $ cd ~
# $ pip3 install adafruit-blinka
# $ pip3 install adafruit-circuitpython-ht16k33
# $ sudo apt install python3-pil

# Import required libraries
import board
from adafruit_ht16k33.segments import Seg7x4
from time import sleep

# Create the display object
i2c = board.I2C()
display = Seg7x4(i2c)

# Set the brightness of the display
display.brightness = 0.5

# Initialize counter/display variable
x = 0

# Loop indefinitely to display the counter
while True:
    # Clear the display and print the counter
    display.print("    ")
    display.print(x)
    
    # Increment the counter
    x += 1
    
    # Reset the counter if it exceeds 9999
    if x > 9999:
        x = 0
        
    # Wait 1 second before updating the display
    sleep(1)