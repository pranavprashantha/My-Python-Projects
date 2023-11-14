# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:40:56 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 6.14 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

def doublefactorial(num):
    if num == 0:
        return 1
    else:
        i = num
        total = num
        while(i > 2):
            total *= i-2
            i -= 2
        return total
    
print(doublefactorial(9))