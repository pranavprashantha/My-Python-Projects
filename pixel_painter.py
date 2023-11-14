# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:18:22 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 11.12 Lab
# Date: 11/08/2023
#
#
# YOUR CODE HERE
#

file_input = input("Enter the filename: ")
add = open(f'{file_input[:-4]}.txt', "w")
file = open(file_input, "r")

char = input("Enter a character: ")

for next_line in file:
    line = next_line.split(",")
    temp = ''
    for i in range(len(line)):
        if i % 2 == 0 :
            temp = temp + " " * int(line[i])
        if i % 2 == 1:
            temp = temp + (char * int(line[i]))
    add.write(temp)
    add.write('\n')
print(f"{file_input[:-4]}.txt created!")
    
add.close()
file.close()
        
    