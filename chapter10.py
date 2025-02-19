"""
5194 Homework 8
Isaac Einstein

Chapter 10 Cookbook Assignment:
Recipe 10.10, Using a Raspberry Squid

Problem Statement:
You want to connect an RGB LED to your Raspberry Pi without having to build something on a breadboard.
"""

# Import required libraries
from gpiozero import RGBLED
from time import sleep
from colorzero import Color

# Declare pins used
redPin = 18
greenPin = 23
bluePin = 24

# Create RGBLED object and set color pins
led = RGBLED(red=redPin, green=greenPin, blue=bluePin)

while(True):
        # Turn on LED and change color
        led.color = Color('red')
        sleep(2)
        led.color = Color('green')
        sleep(2)
        led.color = Color('blue')
        sleep(2)
        led.color = Color('white')
        sleep(2)