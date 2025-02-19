"""
5194 Homework 8
Isaac Einstein

Chapter 13 Cookbook Assignment:
Recipe 13.8, Using a Keypad

Problem Statement:
You want to interface a keypad with your Raspberry Pi.
"""

# Import required libraries
from gpiozero import Button, DigitalOutputDevice
import time

# Declare the rows, columns, and keys of hte keypad
rows = [Button(17), Button(25), Button(24), Button(23)]
cols = [DigitalOutputDevice(27), DigitalOutputDevice(18),
    DigitalOutputDevice(22)]
keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']]

# Function to get the key pressed and read it based on the 'key' matrix
def get_key():
    key = 0
    for col_num, col_pin in enumerate(cols):
        col_pin.off()
        for row_num, row_pin in enumerate(rows):
            if row_pin.is_pressed:
                key = keys[row_num][col_num]
        col_pin.on()
    return key

# loop to get the key pressed and print the output
while True:
    key = get_key()
    if key :
        print(key)
    time.sleep(0.3)