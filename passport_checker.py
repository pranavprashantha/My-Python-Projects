# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:42:49 2023

@author: raopr
"""
'''
While waiting in the security line at the airport to start your amazing international vacation, you
overhear one of the TSA agents state that they’re having trouble with the passport scanner. With your
newly acquired knowledge of reading and writing to files in Python, you agree to help them out.
First, take a look at the file provided to you named scanned_passports.txt. Although initially it looks like
junk, it actually contains information on all of the passports scanned so far. Your job is to figure out
which passports have all of the required fields. The expected fields are 

• byr – Birth year
• iyr – Issue year
• eyr – Expiration year
• hgt – Height
• hcl – Hair color
• ecl – Eye color
• pid – Passport ID
• cid – Country ID

Data for each passport is stored as a sequence of key:value pairs separated by a space or newline,
and each passport scan is separated by a blank line. A valid passport must contain all fields, except for
eye color which is optional. For example,

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

is valid because all eight fields are present. However, the passport

hgt:189cm byr:1987 pid:572028668 iyr:2014 hcl:#623a2f
eyr:2028 ecl:amb

is NOT valid because it is missing cid, the Country ID. The passport

cid:181 eyr:2027 hgt:71in
hcl:#a6e570 pid:166260202 iyr:2016 byr:1918

IS valid because the only missing field is ecl, the eye color field, which is optional.
'''
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

