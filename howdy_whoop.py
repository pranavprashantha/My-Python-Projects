# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:31:32 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 6.13 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
howdy = int(input('Enter an integer: '))
whoop = int(input('Enter another integer: '))

i = 1
while (i < 101):
    if i % howdy != 0 and i % whoop != 0:
        print(i)
    elif i % howdy == 0 and i % whoop != 0:
        print("Howdy")
    elif i % whoop == 0 and i % howdy != 0:
        print("Whoop")
    else:
        print('Howdy Whoop')
    print('\n')
    i += 1