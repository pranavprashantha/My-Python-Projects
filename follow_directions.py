# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:01:44 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 1.13 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import sin
from math import radians

print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print()
print("My guess is 1")
num = 1.1
for x in range(8):
    ans = (sin(num-1))/(num-1)
    print(ans)
    num1 = num // 1
    num2 = (num % 1) / 10
    num = num1 + num2
print()
print("My guess is pretty close")
