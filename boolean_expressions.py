# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:03:32 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 4.15 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

############ Part A ############
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

if a == "True" or a=="t" or a=="T":
    a = True
elif a == "False" or a=="f" or a=="F":
    a = False
else:
    print("Not proper input")
    
if b == b=="True" or b=="t" or b=="T":
    b = True
elif b == "False" or b=="f" or b=="F":
    b = False
else:
    print("Not proper input")
    
if c == "True" or c=="t" or c=="T":
    c = True
elif c == "False" or c=="f" or c=="F":
    c = False
else:
    print("Not proper input")
############ Part B ############
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")
############ Part C ############
XOR = (a and (not b)) or (b and (not a))
print(f"XOR: {XOR}")

Odd = (a and (not b) and (not c)) or (b and (not a) and (not c)) or (c and (not a) and (not b)) or (a and b and c)
print(f"Odd number: {Odd}") # very funny

