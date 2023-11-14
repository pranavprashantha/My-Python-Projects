# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:10:42 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 7.26 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

def replace(letter):
    leet = {
        "a": "4",
        "e": "3",
        "o": "0",
        "s": "5",
        "t": "7"
        }
    if letter in leet:
        return leet[letter]
    else:
        return letter
    
    
inp = input("Enter some text: ")
words = ""
for i in range(len(inp)):
    words += replace(inp[i])
print(f'In leet speak, "{inp}" is:\n{words}')