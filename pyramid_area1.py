# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:35:40 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 6.11 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import *

side = float(input("Enter the side length in meters: "))
n = int(input("Enter the number of layers: "))
numTri = 0
total_area = 0

for i in range(n):
    numTri += (i+1)**2
    
goldOnBase = ((sqrt(3)/4)*(side**2)) * (n**2)
goldOnSide = 0
for i in range(n):
    goldOnSide += ((n-i)*3)*(side**2)

print(f'You need {goldOnBase + goldOnSide:0.2f} m^2 of gold foil to cover the pyramid')
