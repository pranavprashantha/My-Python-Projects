# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:39:49 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 5.4 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import * #Import

temp = float(input("Enter the excess temperature: "))
flux = 0#Input

#Range 1 to 5
if temp > 1 and temp < 5:
    flux = 1000*(temp/1.3)**(log(7)/log(5/1.3))
elif temp >= 5 and temp < 30: #Range 5 to 30
    flux = 7000*(temp/5)**(log(1500000/7000)/log(6))
elif temp >= 30 and temp < 120: #Range 30 to 120
    flux = 1500000*(temp/30)**(log(25000/1500000)/log(4))
elif temp >= 120 and temp <= 1200: #Range 120 to 1200
    flux = 25000*(temp/120)**(log(1500000/25000)/log(10))

if flux != 0:
    flux = round(flux, 0) #Prints it out
    print(f'The surface heat flux is approximately {flux:1.0f} W/m^2')
else: #Error
    print("Surface heat flux is not available")