# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:13:24 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 6.16 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
num = int(input("Enter a value for n: "))
bottom = 0
for i in range(num-1):
    bottom += i+1

top = 0
equal = False
i = num+1
count = 0
while (top < bottom):
    top += i
    i += 1
    count += 1
    if (top == bottom):
        equal = True

if(equal):
    print(f'{num} is a balancing number with r={count}')
else:
    print(f'{num} is not a balancing number')