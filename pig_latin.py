# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:46:24 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 7.25 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#
def vowel(num):
    if (num == 'a' or num == 'e' or num == 'i' or num == 'o' or num == 'u' or num == "y"):
        return True
    return False
def firstVowel(word):
    for i in range(len(word)):
        if vowel(word[i]):
            return i
    return


inp = input("Enter word(s) to convert to Pig Latin: ")
words = inp.split()
out = ""

for i in range(len(words)):
    temp = words[i]
    if not (vowel(temp[0])):
        first = firstVowel(temp)
        out += temp[(first):] + temp[0:first] + "ay"
    else:
        out += temp + "yay"
    out += " "
print(f'In Pig Latin, "{inp}" is: {out}')          
        
                
    