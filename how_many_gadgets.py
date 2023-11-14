# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:39:15 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 4.18 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

day = int(input("Please enter a positive value for day: "))
if day > 0:
    if day >= 10:
        gadget = 100
        if day >= 50:
            gadget += 400+(40*41/2)
            if day > 100:
                gadget += 2500
            else:
                gadget += (day-50)*50
        else:
            gadget += (day-10)*10 + ((day-10)*(day-9)/2)
    else: 
        gadget = 10*day
    print("The sum total number of gadgets produced on day",day,"is",int(gadget))
    
else:
    print("You entered an invalid number!")