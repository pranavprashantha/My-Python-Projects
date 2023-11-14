# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:33:11 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 4.19 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import *

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))


if a==0 and b==0 and c!=0:
    print("You entered an invalid combination of coefficients!")
elif a==0:
    print(f"The root is x = {-c/b}")
else:
    mid = b**2 - 4*a*c
    if mid < 0:
        print(f"The roots are x = {-b/2*a} + {sqrt(abs(mid))/2*a:0.1f}i and x = {-b/2*a} - {sqrt(abs(mid))/2*a:0.1f}i")
    else:
        root1 = -b/2*a + sqrt(mid)/2*a
        root2 = -b/2*a - sqrt(mid)/2*a
        if(root1 != root2):
            print(f"The roots are x = {-b/2*a + sqrt(mid)/2*a:0.1f} and x = {-b/2*a - sqrt(mid)/2*a:0.1f}")
        else:
            print(f"The root is x = {-b/2*a + sqrt(mid)/2*a:0.1f}")