# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:05:01 2023

@author: raopr
"""

'''
The first measurement was taken at time 𝑡 = 10 minutes, and the second was taken 45 minutes later. At the
first measurement, the ISS was 2,027 kilometers past Houston, TX. At the second measurement, the ISS was
23,027 kilometers past Houston.

Write a program that determines, for any time between 10 and 55 minutes, where the ISS will be (in
terms of kilometers past Houston). The time to evaluate at should be a variable in your program. The
program should print both the time and the position at that time to the screen, with a line describing
what is being output (see example output below). You should test your program at various times and
make sure the results seem reasonable.

For your final program that you submit, output the position at a time of 25 minutes. (Next week, we
will see how you can read in numbers from a user, but for now, just assume it is a fixed number of
minutes.)
'''

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


