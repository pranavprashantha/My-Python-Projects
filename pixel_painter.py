# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:18:22 2023

@author: raopr
"""

'''
Run length encoding is a form of data storage where runs of data are stored as a single data value. A run of
data is a sequence of the same value that occurs in many consecutive elements. This type of data storage is
efficient for simple graphic images such as icons, line drawings, and Conway’s Game of Life. For this activity,
consider a binary image where each pixel is either light (a space) or dark (a character). Each line of the image is
represented by comma separated values that indicate the number of consecutive pixels that are light and dark.
The first value in a line always corresponds to the number of light pixels, and following values alternate
between dark and light. For example, the line 1,2,3,4 represents 1 light pixel, followed by 2 dark pixels, 3
light pixels, and finally 4 dark pixels. If a space is used to represent light pixels and the character O is used to
represent dark pixels, the line would look like this (spaces underlined for clarity): _OO___OOOO

Write a program named pixel_painter.py that takes as input a filename and a character, converts the contents
of the file to pixel art using a space for light pixels and the entered character for dark pixels, and writes the art
to a new file of the same name but with the .txt extension
'''
file_input = input("Enter the filename: ")
add = open(f'{file_input[:-4]}.txt', "w")
file = open(file_input, "r")

char = input("Enter a character: ")

for next_line in file:
    line = next_line.split(",")
    temp = ''
    for i in range(len(line)):
        if i % 2 == 0 :
            temp = temp + " " * int(line[i])
        if i % 2 == 1:
            temp = temp + (char * int(line[i]))
    add.write(temp)
    add.write('\n')
print(f"{file_input[:-4]}.txt created!")
    
add.close()
file.close()
        
    
