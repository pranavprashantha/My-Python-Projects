# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:13:36 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 3.17 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import *

print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
acceleration = float(input("Please enter the acceleration (m/s^2): "))
print(f"Force is {mass*acceleration:0.1f} N")
print()
#Q2
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
print(f"Wavelength is {2*distance*sin(radians(angle)):0.4f} nm")
print()

#Q3
print("This program calculates how much Radon-222 is left given time and initial amount")
left = float(input("Please enter the time (days): "))
init_amount = float(input("Please enter the initial amount (g): "))
half_life = 3.8
print(f"Radon-222 left is {(init_amount*(2**((-1*left)/half_life))):0.2f} g")
print()

#Q4
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temp = float(input("Please enter the temperature (K): " ))
constant = 8.314
print(f"Pressure is {((moles*temp*constant)/volume)/1000:.0f} kPa")
print()