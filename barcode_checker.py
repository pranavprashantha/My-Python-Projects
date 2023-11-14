# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:31:56 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 11.11 Lab
# Date: 11/08/2023
#
#
# YOUR CODE HERE
#

#Takes in file input
file_input = input("Enter the name of the file: ")
file = open(file_input, "r")
add = open('valid_barcodes.txt', 'w')

count = 0
for next_line in file:
    list1 = []
    list2 = []
    for i in range(12):
        if(i % 2 == 0):
            list1.append(int(next_line[i]))
        else:
            list2.append(int(next_line[i]))
    sum1 = sum(list1)
    sum2 = sum(list2)
    step2 = sum2 * 3
    step3 = step2 + sum1
    step4 = 10 - int(str(step3)[-1])
    if next_line[-1] == '\n':
        if step4 == int(next_line[-2]):
            count+=1
            add.write(next_line)
    else:
        if step4 == int(next_line[-1]):
            count+=1
            add.write(next_line)
            
print(f'There are {count} valid barcodes')

file.close()
add.close()