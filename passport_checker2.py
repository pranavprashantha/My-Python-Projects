# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:36:41 2023

@author: raopr
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 11.10 Lab
# Date: 11/08/2023
#
#
# YOUR CODE HERE
#

#opens file inputed by user
file_input = input("Enter the name of the file: ")
add = open("valid_passports2.txt", "w")
file = open(file_input, "r")

valid = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "pid:", "cid:"]

#formatting everything to an unique array
line = file.read()
passport_arr = line.split("\n")
new_passport_arr = []
valids = []
chars = "0123456789abcdef"
j = 0

for i in range(len(passport_arr)):
    temp1 = ""
    break_out_flag = False
    while True:
        if passport_arr[j] != '':
            temp1 = temp1 + passport_arr[j] + "\n"
            if j == len(passport_arr)-1:
                new_passport_arr.append(temp1)
                break_out_flag = True
                break
            j+=1
        else:
            new_passport_arr.append(temp1)
            j+=1
            break
    if break_out_flag:
        break
    
def checker(each):
    if("byr" in each[0]):
        if not(len(each[1]) == 4) or not(1920 <= int(each[1]) <= 2007):
            return False
    if("iyr" in each[0]):
        if not(len(each[1]) == 4) or not(2013 <= int(each[1]) <= 2023):
            return False
    if("eyr" in each[0]):
        if not(len(each[1]) == 4) or not(2023 <= int(each[1]) <= 2033):
            return False    
    if("hgt" in each[0]):
        if "in" in each[1]:  
            temp = int(each[1].split("in")[0])
            if (not(int(temp) >= 59 and int(temp) <= 76)):
                return False
        elif "cm" in each[1]:
            temp = int(each[1].split("cm")[0])
            if (not(int(temp) >= 150 and int(temp) <= 193)):
                return False
        else:
            return False
    if("hcl" in each[0]):
        if not(len(each[1][1:]) == 6) or not(each[1][0] == "#"):
            return False
        x = 0
        for i in range(1, len(each[1])):
            if each[1][i] in chars:
              x += 1
        if x != 6:
          return False;
    if("pid" in each[0]):
         if not(len(str(each[1])) == 9):
             return False
    if("cid" in each[0]):
         if not(len(each[1]) == 3) or not(int(each[1]) >= 100 and int(each[1]) < 1000):
             return False
    return True
        
        
        
count = 0
for i in range(len(new_passport_arr)):
    flo = True
    for j in range(len(valid)):
        if (new_passport_arr[i].find(valid[j]) == -1):
            flo = False
    if flo:
        valids.append(new_passport_arr[i])
for temp2 in valids:
    flo2 = True
    temp3 = temp2.replace('\n', ' ')
    section = temp3.split()
    
    for k in section:
        each = k.split(':')
        hold = checker(each)
        if not hold:
            flo2 = False
                
    if flo2:
        add.write(temp2)
        add.write("\n")
        count+=1
print(f'There are {count} valid passports')
add.close()
file.close()
            
        
