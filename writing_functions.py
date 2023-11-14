# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:47:17 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 3.18 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import *

def tri(side):
    return((side**2)*(sqrt(3)/4))

def square(side):
    return side**2

def pent(side):
    return (1/4)*sqrt(5*(5+(2*sqrt(5)))) * side**2

def dod(side):
    return 3*(2+sqrt(3))*side**2

side = float(input("Please enter the side length: "))
print(f"A triangle with side {side:0.2f} has area {tri(side):0.3f}")
print(f"A square with side {side:0.2f} has area {square(side):0.3f}")
print(f"A pentagon with side {side:0.2f} has area {pent(side):0.3f}")
print(f"A dodecagon with side {side:0.2f} has area {dod(side):0.3f}")