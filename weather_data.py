# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:02:31 2023

@author: raopr
"""

'''
On Canvas, there is a CSV file posted with this assignment named WeatherDataCLL.csv that contains weather
data from Easterwood Airport (in College Station) for 10 years. The data was taken from the National Oceanic
and Atmospheric Administration’s National Centers for Environmental Information1. You can view the data by
opening the file in any text or spreadsheet editor (e.g. Notepad++, Excel) or in your IDE. The first line of the file
contains the column headers explaining what each column is. Note: Some days are missing data.
Download the file and write a program named weather_data.py that does the following:

1. Open the CSV file for reading
2. Read the CSV file and compute
    a. the maximum temperature seen over the 10-year period
    b. the minimum temperature seen over the 10-year period
3. Output the results to the console using the format below
4. Perform the following three data analysis exercises and output the results to the console. Take as input
from the user a month and year, then for that month,
    a. Calculate the mean of the average temperatures (use 1 decimal place)
    b. Calculate the mean relative humidity (use 1 decimal place)
    c. Calculate the mean daily wind speed (use 2 decimal places)
    d. Calculate the percentage of days with non-zero precipitation (use 1 decimal place)
'''

#open file
file = open("WeatherDataCLL.csv", "r")
#min and max
lines = file.readlines()
#print(lines)
lines.pop(0)
minTemp = 1000
maxTemp = 0
for i in lines:
    line = i.split(",")
    if line[6] != "" and line[6] != "\n":
        minLine = int(line[6])
        if minLine < minTemp:
            minTemp = minLine
    if line[5] != "" and line[5] != "\n":
        maxLine = int(line[5])
        if maxLine > maxTemp:
            maxTemp = maxLine
print(f'10-year maximum temperature: {maxTemp} F')
print(f'10-year minimum temperature: {minTemp} F')
#average for month and year
monthDict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

monthIn = input("Please enter a month: ")
year = int(input("Please enter a year: "))

month = monthDict[monthIn]
dayCount = 0
avgTemp = 0
avgHum = 0
avgWind = 0
avgPrec = 0

for i in lines:
    line = i.split(',')
    date = line[0]
    dateSplit = date.split('/')
    if int(dateSplit[0]) == month and int(dateSplit[2]) == year:
        if line[4] != "":
            avgTemp += float(line[4])
        if line[3] != "":
            avgHum += float(line[3])
        if line[1] != "":
            avgWind += float(line[1])
        if line[2] != "":
            if float(line[2]) > 0:
                avgPrec += 1
        dayCount += 1
        
print(f'For {monthIn} {year}:')
print(f'Mean average daily temperature: {avgTemp/dayCount: .1f} F')
print(f'Mean relative humidity: {avgHum/dayCount: .1f}%')
print(f'Mean daily wind speed: {avgWind/dayCount: .2f} mph')
print(f'Percentage of days with precipitation: {(avgPrec/dayCount)*100:.1f}%')

