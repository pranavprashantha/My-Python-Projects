# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:31:56 2023

@author: raopr
"""

'''
A barcode is valid if the digits satisfy a certain constraint. For example, take the 13-digit barcode
1877455846014 and split the first 12 digits into two groups: (1,7,4,5,4,0) and (8,7,5,8,6,1).
The first group contains every other digit starting with the first, and the second group contains every other
digit starting with the second. Take the sum of the digits in the second group, and multiply it by 3. Add to that
the sum of the digits in the first group. Subtract the last digit of that number from 10, and it should match the
last digit of the barcode.

Example math using barcode 1877455846014:
Sum of first group = 1 + 7 + 4 + 5 + 4 + 0 = 21
Sum of second group = 8 + 7 + 5 + 8 + 6 + 1 = 35
Multiply second group by 3 = 35 x 3 = 105
Add first group = 105 + 21 = 126
Use the last digit and subtract from ten = 10 - 6 = 4
4 is the last digit in the barcode, so it is valid

Write a program named barcode_checker.py that takes as input a filename that contains many 13-digit
barcodes. Have your program read the file, determine whether each barcode is valid, and write the valid
barcodes to a new file named valid_barcodes.txt. Have your program output the total number of valid
barcodes found using the example output below. You do not have to submit your valid_barcodes.txt file to
zyBooks.

'''
#Takes in file input
file_input = input("Enter the name of the file: ")
file = open(file_input, "r")
add = open('valid_barcodes.txt', 'w')

count = 0
for next_line in file:
    list1 = []
    list2 = []
    for i in range(12):
        if(i % 2 == 0):
            list1.append(int(next_line[i]))
        else:
            list2.append(int(next_line[i]))
    sum1 = sum(list1)
    sum2 = sum(list2)
    step2 = sum2 * 3
    step3 = step2 + sum1
    step4 = 10 - int(str(step3)[-1])
    if next_line[-1] == '\n':
        if step4 == int(next_line[-2]):
            count+=1
            add.write(next_line)
    else:
        if step4 == int(next_line[-1]):
            count+=1
            add.write(next_line)
            
print(f'There are {count} valid barcodes')

file.close()
add.close()
