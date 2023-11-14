# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:56:30 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 2.9 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import *

# Q1
mass = 27
acceleration = 1.5
print("Force is",mass*acceleration,"N")

#Q2
distance = 0.025
angle = 35
print("Wavelength is",2*distance*sin(radians(angle)),"nm")

#Q3
init_amount = 27
half_life = 3.8
left = 5
print("Radon-222 left is",(init_amount*(2**((-1*left)/half_life))),"g")

#Q4
moles = 5
volume = 0.27
temp = 415
constant = 8.314
print("Pressure is",((moles*temp*constant)/0.27)/1000,"kPa")