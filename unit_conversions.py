# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Pranav Rao
# Section: 564
# Assignment: 3.17 Lab
# Date: 08/24/2023
#
#
# YOUR CODE HERE
#

def pounds(x):
    x*=4.4482216152605
    return x

def meters(x):
    x*=3.280839895
    return x

def atmosphere(x):
    x*=101.325
    return x

def watts(x):
    x*=3.41214163
    return x

def liters(x):
    x*=0.264172052
    x*=60
    return x

def degrees(x):
    x*=(9/5)
    x+=32
    return x

user_input = float(input("Please enter the quantity to be converted: "))
print((f'{user_input:0.2f}'), "pounds force is equivalent to", (f'{pounds(user_input):0.2f}'), "Newtons")
print((f'{user_input:0.2f}'), "meters is equivalent to", (f'{meters(user_input):0.2f}'), "feet")
print((f'{user_input:0.2f}'), "atmospheres is equivalent to", (f'{atmosphere(user_input):0.2f}'), "kilopascals")
print((f'{user_input:0.2f}'), "watts is equivalent to", (f'{watts(user_input):0.2f}'), "BTU per hour")
print((f'{user_input:0.2f}'), "liters per second is equivalent to", (f'{liters(user_input):0.2f}'), "US gallons per minute ")
print((f'{user_input:0.2f}'), "degrees Celsius is equivalent to", (f'{degrees(user_input):0.2f}'), "degrees Fahrenheit")


