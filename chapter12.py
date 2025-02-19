"""
5194 Homework 8
Isaac Einstein

Chapter 12 Cookbook Assignment:
Recipe 12.1, Controlling Servomotors

Problem Statement:
You want to use a Raspberry Pi to control the position of a servomotor.
"""
# Import required libraries
from gpiozero import AngularServo
from guizero import App, Slider

# Create the servo object
servo = AngularServo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

# Function to change the angle of the servo
def slider_changed(angle):
    servo.angle = int(angle)   
    
# Create the GUI
app = App(title='Servo Angle', width=500, height=150)
slider = Slider(app, start=-90, end=90, command=slider_changed, width='fill',
                height=50)
slider.text_size = 30
app.display()