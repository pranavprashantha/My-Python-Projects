# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:25:07 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 7.27 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

def addLists(lists):
    fin = 0
    for i in range(len(lists)):
        fin += lists[i]
    return fin
def check(list1, list2):
    num1 = addLists(list1)
    num2 = addLists(list2)
    if num1 == num2:
        return True
    return False

lists = input("Enter numbers: ")
words = lists.split()
nums = []
for i in range(len(words)):
    nums.append(int(words[i]))

for i in range(len(nums)):
    list1 = nums[0:i+1]
    list2 = nums[i+1:]
    if check(list1, list2):
        index = i
        fin1 = list1
        fin2 = list2
        break
    else:
        index = -1
    
if index != -1:
    print(f'Left: {fin1}\nRight: {fin2}\nBoth sum to {addLists(fin1)}')
else:
    print('Cannot split evenly')
    
