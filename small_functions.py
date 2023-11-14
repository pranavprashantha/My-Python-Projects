# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:49:06 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Pranav Rao
# Section:      564
# Assignment:   9.16
# Date:         10/25/2023
from math import*
# Part A
def parta (rSphere, rCylinder):
    #volume of sphere
    volume = (4/3)*pi*rSphere**3
    rh = sqrt(rSphere**2 - rCylinder**2)
    h = rSphere-rh
    endcap = (1/6)*pi*h*((3*(rCylinder**2))+(h**2))
    vCylinder = pi * (rCylinder)**2*rh
    v2 = 2* (endcap + vCylinder)
    return volume - v2
#Part B
def partb(n):
    #odd nums list
    oddNums = []
    for i in range(1, n // 2, 2):
        oddNums = []
        temp = i
        total = 0
        while total < n:
            oddNums.append(temp)
            total += temp
            temp += 2
        if total == n:
            return oddNums
    return False
#Part C
def partc(letter, name, company, email):
    #Find max length
    fin = ''
    info = [letter, name, company, email]
    length = 0
    for i in range(4):
        if len(info[i]) > length:
            length = len(info[i])
    length += 4
    fin += str(letter * (length + 2)) + '\n'
    fin += letter + str(' ' * ((length - len(name)) // 2)) + name + str(' ' * (length -((length - len(name)) // 2 + len(name)))) + letter + '\n'
    fin += letter + str(' ' * ((length - len(company)) // 2)) + company + str(' ' *(length - ((length - len(company)) // 2 + len(company)))) + letter + '\n' 
    fin += letter + str(' ' * ((length - len(email)) // 2)) + email + str(' ' * (length- ((length - len(email)) // 2 + len(email)))) + letter + '\n'
    fin += str(letter * (length + 2))
    return fin
#Part D
def partd(numList):
    #Sort the list
    numList.sort()
    length = len(numList)
    if length % 2 == 0:
        median = (numList[int(length / 2)] + numList[int(length / 2) - 1]) / 2
    else:
        median = numList[int(length / 2)]
    return numList[0], median, numList[length - 1]
#Part E
def parte(time, distance):
    #vel for velocity
    if len(time) != len(distance):
        return False
    vel = []
    i = 1
    while i < len(time):
        tDiff = time[i] - time[i-1]
        dDiff = distance[i] - distance[i-1]
        
        if tDiff != 0:
            vel.append(dDiff / tDiff)
        else:
            vel.append(float('inf'))
        i+=1
    return vel
#Part F
def partf(nums):
    #see if it adds to 2027
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == 2027:
                return nums[i] * nums[j]
    return False
def partG(x, tolerance):
    return True