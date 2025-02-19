"""
5194 Homework 8
Isaac Einstein

Chapter 16 Cookbook Assignment:
Recipe 16.7, Making a Buzzing Sound

Problem Statement:
You want to make a buzzing sound with the Raspberry Pi.
"""

# Import required libraries
from gpiozero import Buzzer

# Create a Buzzer object
buzzer = Buzzer(18)

# Function to buzz the buzzer
def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    buzzer.beep(on_time=period, off_time=period, n=int(cycles/2))

# Loop to get the pitch and duration and buzz the buzzer
while True:
    # Gather user input
    pitch_s = input("Enter Pitch (200 to 2000): ")
    pitch = float(pitch_s)
    duration_s = input("Enter Duration (seconds): ")
    duration = float(duration_s)
    
    # Call buzz function with user input
    buzz(pitch, duration)

