# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:35:19 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 4.14 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))
fin = ""

if A > 0:
    if A > 1:
        fin += str(abs(A))+"x^2"
    elif A == 1:
        fin += "x^2"
elif A < 0:
    if A < -1:
        fin += "- "+str(abs(A))+"x^2"
    elif A == -1:
        fin += "- x^2"

if B > 0:
    if B > 1 and A == 0:
        fin += str(abs(B))+"x"
    elif B > 1:
        fin += " + "+str(abs(B))+"x"
    elif B == 1 and A == 0:
        fin += "x"
    elif B == 1:
        fin += " + x"
elif B < 0:
    if(B < -1):
        fin += " - " + str(abs(B)) + "x"
    elif B == -1:
        fin += " - x"

if(C > 0):
    fin += " + " + str(abs(C))
elif C < 0:
    fin += " - " + str(abs(C))

print("The quadratic equation is", fin,"= 0")