# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:05:01 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 2.8 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
from math import *
import numpy as np

start_time = 10
end_time = 55
start_pos = 2027
end_pos = 23027
velocity = (end_pos-start_pos)/(end_time-start_time)

time = np.array([25, 300])
for i in range(time.shape[0]):
    pos = (velocity*(time[i]-start_time)+start_pos) % (2*pi*6745)
    print("Part "+str(i+1) + ":\nFor t =",time[i],"minutes, the position p =",pos,"kilometers")


