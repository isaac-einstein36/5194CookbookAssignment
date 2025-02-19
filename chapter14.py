"""
5194 Homework 8
Isaac Einstein

Chapter 14 Cookbook Assignment:
Recipe 14.11, Measuring the Raspberry Pi CPU Temperature

Problem Statement:
You want to know just how hot your Raspberry Pi’s CPU is getting.
"""
# Import required libraries
import time
from gpiozero import CPUTemperature

# Loop to get the CPU temperature and print it
while True:
    # Find temp in celsius
    cpu_temp = CPUTemperature()
    
    # Convert to fahrenheit
    cpu_temp_f = cpu_temp.temperature * 9/5 + 32
    
    # Print results in a formatted string
    print(f"Temperature:\n\t{cpu_temp.temperature}°C\n\t{cpu_temp_f}°F")
    time.sleep(1)