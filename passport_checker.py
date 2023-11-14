# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:42:49 2023

@author: raopr
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 11.9 Lab
# Date: 11/08/2023
#
#
# YOUR CODE HERE
#

#opens file inputed by user
file_input = input("Enter the name of the file: ")
add = open("valid_passports.txt", "w")
file = open(file_input, "r")

valid = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "pid:", "cid:"]

#formatting everything to an unique array
line = file.read()
passport_arr = line.split("\n")
new_passport_arr = []
valid_passports = []

j = 0

for i in range(len(passport_arr)):
    temp = ""
    break_out_flag = False
    while True:
        if passport_arr[j] != '':
            temp = temp + passport_arr[j] + "\n"
            if j == len(passport_arr)-1:
                new_passport_arr.append(temp)
                break_out_flag = True
                break
            j+=1
        else:
            new_passport_arr.append(temp)
            j+=1
            break
    if break_out_flag:
        break

count = 0
for i in range(len(new_passport_arr)):
    flo = True
    for j in range(len(valid)):
        if (new_passport_arr[i].find(valid[j]) == -1):
            flo = False
    if flo:
        add.write(new_passport_arr[i])
        add.write('\n')
        count += 1
add.close()
file.close()
print(f'There are {count} valid passports')

