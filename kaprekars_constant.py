# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:59:51 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 7.28 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

def four(num):
    if len(str(num)) == 4:
        return num
    if len(str(num)) == 3:
        return int("0" + str(num))
    if len(str(num)) == 2:
        return int("00" + str(num))
    if len(str(num)) == 1:
        return int("000" + str(num))
def sort(num):
    one = num // 1000
    num = num % 1000
    two = num // 100
    num = num % 100
    three = num // 10
    num = num % 10
    four = num
    
    lists = [one, two, three, four]
    descending = sorted(lists, reverse = True)
    ascending = sorted(lists)
    
    des_num = ""
    asc_num = ''
    for i in range(len(descending)):
        des_num += str(descending[i])
        asc_num += str(ascending[i])
    
    asc = int(asc_num)
    des = int(des_num)
    
    return des, asc

num = int(input("Enter a four-digit integer: "))
init = num
out = f"{num} > "
count = 0

while num != 6174:
    second, first = sort(four(num))
    num = second - first
    count+=1
    if num != 6174 and num != 0:
        out += f"{num} > "
    elif num == 0:
        out += f"{num}"
        break
    else:
        out += str(num)
print(out)
if num == 6174:
    print(f"{init} reaches 6174 via Kaprekar's routine in {count} iterations")
else:
    print(f"{init} reaches 0 via Kaprekar's routine in {count} iterations")
    
    
    
    
    
    
    
    
    