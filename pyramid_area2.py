# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:21:06 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 6.12 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
from math import *

side = float(input("Enter the side length in meters: "))
n = int(input("Enter the number of layers: "))

goldOnBase = ((sqrt(3)/4)*(side**2)) * (n**2)
goldOnSide = (n)*((n-1)*(1.5)+3)*(side**2)

print(f'You need {goldOnBase + goldOnSide:0.2f} m^2 of gold foil to cover the pyramid')