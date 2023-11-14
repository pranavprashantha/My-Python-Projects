# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:34:56 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 3.16 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

t1 = float(input("Enter time 1: \n"))
p1x = float(input("Enter the x position of the object at time 1: \n"))
p1y = float(input("Enter the y position of the object at time 1: \n"))
p1z = float(input("Enter the z position of the object at time 1: \n"))
t2 = float(input("Enter time 2: \n"))
p2x = float(input("Enter the x position of the object at time 2: \n"))
p2y = float(input("Enter the y position of the object at time 2: \n"))
p2z = float(input("Enter the z position of the object at time 2: \n"))

pos1 = [p1x,p1y,p1z]
pos2 = [p2x,p2y,p2z]

time = t1

for j in range(5):
    out = f"At time {time:.2f} seconds the object is at ("
    for i in range(3):
        start_pos = pos1[i]
        end_pos = pos2[i]
        velocity = (end_pos-start_pos)/(t2-t1)
        pos = (velocity*(time-t1)+start_pos)
        if i < 2:
            out += f"{pos:.3f}, "
        else:
            out += f"{pos:.3f})"
    print(out)            
    time = time + (t2-t1)/4


