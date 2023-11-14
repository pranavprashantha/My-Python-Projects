# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:10:21 2023

@author: raopr
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 4.13 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
print(f"You received ${pay-cost:0.2f} in change. That is...")
pay *= 10000
cost *= 10000
temp = pay-cost

quarters = 0
dime = 0
nickel = 0
penny = 0

if temp >= 2500:
    quarters = temp // 2500
    temp = temp % 2500
if temp >= 1000:
    dime = temp // 1000
    temp = temp % 1000
if temp >= 500:
    nickel = temp // 500
    temp = temp % 500
if temp >- 100:
    penny = temp // 100
    temp = temp % 100
    
if(quarters != 0):
    if quarters == 1:
        print(str(int(quarters)) + " quarter")
    else: 
        print(str(int(quarters)) + " quarters")
if(dime != 0):
    if dime == 1:
        print(str(int(dime)) + " dime")
    else:
        print(str(int(dime)) + " dimes")
if (nickel != 0):
    if nickel == 1:
        print(str(int(nickel)) + " nickel")
    else:
        print(str(int(nickel)) + " nickel")
if penny != 0:
    if penny == 1:
        print(str(int(penny)) + " penny")
    else:
        print(str(int(penny)) + " pennies")