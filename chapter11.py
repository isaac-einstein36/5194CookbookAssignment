"""
5194 Homework 8
Isaac Einstein

Chapter 11 Cookbook Assignment:
Recipe 10.11, Using a Raspberry Squid

Problem Statement:
You want to make an application to run on the Raspberry Pi that has a slider to control power to a device using pulse-width modulation (PWM)
"""

# Import required libraries
from gpiozero import PWMOutputDevice 
from guizero import App, Slider

# Declare the output pin
pin = PWMOutputDevice(18)

# Function to change the PWM value of the LED
def slider_changed(percent):
    pin.value = int(percent) / 100  

# Create the GUI
app = App(title='PWM', width=500, height=150)
slider = Slider(app, command=slider_changed, width='fill', height=50)
slider.text_size = 30
app.display()