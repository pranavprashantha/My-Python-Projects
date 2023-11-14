# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:49:31 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 4.16 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#


num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
if num1 >= num2 and num1 >= num3:
    max = num1
elif num2 >= num3:
    max = num2
else:
    max = num3
print("The largest number is", max)
