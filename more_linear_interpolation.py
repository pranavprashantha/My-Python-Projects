# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:34:15 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 2.10 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import *

start_time = 12
x1 = [8,6,7]
end_time = 85
x2 = [-5, 30, 9]
time = 30.0
coord = ['x','y','z']

for j in range(5):
    print("At time",time,"seconds:")
    for i in range(3):
        start_pos = x1[i]
        end_pos = x2[i]
        velocity = (end_pos-start_pos)/(end_time-start_time)
        pos = (velocity*(time-start_time)+start_pos) 
        print(coord[i]+str(j+1)+" =",pos,"m")
    time += 7.5
    if(j < 4):
        print("-----------------------")