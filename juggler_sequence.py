# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:53:11 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 6.15 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

from math import *

count = 0

num = int(input('Enter a positive integer: '))
init = num
print(f'The Juggler sequence starting at {init} is:')
print(num, end = "")

while(num != 1):
    if(num % 2 == 0):
        num = int(sqrt(num))
    else:
        num = int(pow(num, 1.5))
    print(",",num,end = "")
    count+=1

print(f'\nIt took {count} iterations to reach 1')

