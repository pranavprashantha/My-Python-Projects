# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:36:41 2023

@author: raopr
"""
'''
The security line is now moving at lightning speed! But now the TSA agents are worried that some of the
“valid” passports are actually invalid. It turns out that each of those required fields has rules about what
values are valid. 

• byr – Birth year – four digits, between 1920 and 2007, inclusive
• iyr – Issue year – four digits, between 2013 and 2023, inclusive
• eyr – Expiration year – four digits, between 2023 and 2033, inclusive
• hgt – Height – a number followed by either cm or in
o If cm, the number must be between 150 and 193, inclusive
o If in, the number must be between 59 and 76, inclusive
• hcl – Hair color – a # followed by exactly 6 characters (0-9 or a-f)
• ecl – Eye color – not required
• pid – Passport ID – a nine-digit number, including leading zeroes
• cid – Country ID – a three-digit number, NOT including leading zeroes 

Write a program named passport_checker2.py that takes as input from the user a filename, reads the
file, counts the number of valid passports based on the rules above, then writes the valid passport scans
to a new file named valid_passports2.txt. Format your program’s output and your new file using the
same format as Part A.

'''
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
            
        
