#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Madison 
# Liz 
# Adam
# Pranav
# Section: 564
# Assignment: team lab 8
# Date: 10/17/2023
#
#
# YOUR CODE HERE
#

final = [ [],[],[],[],[]]


def numbers(num, main_list): #takes an integer and returns the ASCII symbol
      #the main list variable holds all of the numbers together so that they can be
      #printed out horizontally, not vertically
      #main_list is the list that holds all the ascii symbols
      #symbols are assigned by rows so numbers print out in a line, not one at a time
    if num ==1:
        main_list[0].append(' 1 ') # index 0 holds the first row of symbols for all the numbers
        main_list[1].append('11 ') # index 1 holds the second row
        main_list[2].append(' 1 ') # index 2 holds the middle row 
        main_list[3].append(' 1 ') # index 3 holds the fourth row 
        main_list[4].append('111') # index 4 holds the fifth row
  
    elif num ==2:  #if-elif statements are used to go through every possible number
        main_list[0].append('222')
        main_list[1].append('  2')
        main_list[2].append('222')
        main_list[3].append('2  ')
        main_list[4].append('222')
    elif num ==3:
        main_list[0].append('333')
        main_list[1].append('  3')
        main_list[2].append('333')
        main_list[3].append('  3')
        main_list[4].append('333')
    elif num ==4:
        main_list[0].append('4 4')
        main_list[1].append('4 4')
        main_list[2].append('444')
        main_list[3].append('  4')
        main_list[4].append('  4')
    elif num ==5:
        main_list[0].append('555')
        main_list[1].append('5  ')
        main_list[2].append('555')
        main_list[3].append('  5')
        main_list[4].append('555')
    elif num ==6:
        main_list[0].append('666')
        main_list[1].append('6  ')
        main_list[2].append('666')
        main_list[3].append('6 6')
        main_list[4].append('666')
    elif num ==7:
        main_list[0].append('777')
        main_list[1].append('  7')
        main_list[2].append('  7')
        main_list[3].append('  7')
        main_list[4].append('  7')
    elif num ==8:
        main_list[0].append('888')
        main_list[1].append('8 8')
        main_list[2].append('888')
        main_list[3].append('8 8')
        main_list[4].append('888')
    elif num ==9:
        main_list[0].append('999')
        main_list[1].append('9 9')
        main_list[2].append('999')
        main_list[3].append('  9')
        main_list[4].append('999')
    elif num == 0:
        main_list[0].append('000')
        main_list[1].append('0 0')
        main_list[2].append('0 0')
        main_list[3].append('0 0')
        main_list[4].append('000')
        
    
  

    return main_list 

def layout(symbol):
    #only prints one symbols at a time
    for i in range(len(symbol)): # prints out the ASCII symbols without brackets
        for j in range(len(symbol[i])):
            if j == len(symbol[i])-1:  #if the last symbol, it doesn't have the space at the end.
                print(symbol[i][j])
            else:
                print(symbol[i][j] , end= ' ')
            
                
    
        
        
def symbol_change(symbol, new_character):
# prints out the ASCII symbols without brackets    
      for i in range(len(symbol)):    #finds the length of the list
        temp_string ='' 
        for j in range(len(symbol[i])): # goes through each sublist
            temp_string ='' 
            for k in (symbol[i][j]): #finds every character in the sublist
                if k == ' ' :
                    temp_string += ' ' #keeps the spaces correct
                elif k ==':':
                    temp_string += ':'
                        
                else:
                    temp_string += new_character #makes all other symbols into the right symbol
                symbol[i][j] =temp_string  #reassigns each sublist to have the correct symbol
    
      return symbol 



def strToInt(time):
    time = time.split(":")
    fin_time = []
    for i in range(len(time)):
        temp = time[i]
        length = len(time[i])
        index = 0
        while (index != length):
            num = int(temp[index:index+1])
            fin_time.append(num)
            index+=1
    return fin_time

def AM_or_PM(time_list, main_list):

    if len(time_list) == 3:
        main_list[0].append(' A  M   M')
        main_list[1].append('A A MM MM')
        main_list[2].append('AAA M M M')
        main_list[3].append('A A M   M')
        main_list[4].append('A A M   M')
    elif len(time_list) == 4:
        num = int(str(time_list[0]) + str(time_list[1]))
        if num // 12 == 0:
            main_list[0].append(' A  M   M')
            main_list[1].append('A A MM MM')
            main_list[2].append('AAA M M M')
            main_list[3].append('A A M   M')
            main_list[4].append('A A M   M')
        elif num // 12 == 1:
            main_list[0].append('PPP M   M')
            main_list[1].append('P P MM MM')
            main_list[2].append('PPP M M M')
            main_list[3].append('P   M   M')
            main_list[4].append('P   M   M')


# here we are figuring out what the input is, did they input the 12hr type or 24hr type:
time = (input('Enter the time: '))
#Now they must choose the clock type: 
ctype = (input('Choose the clock type (12 or 24): '))
character = (input("Enter your preferred character: "))
#IF THEY INPUT A CHARACTER USE CHAR TO PRINT OUT NUMBER, ELSE PRINT NUMBER USING NUMBER.
#if they input a symbol the symbol must be part of the list. 
permitted = ['a','b','c','d','e','g','h','k','m','n','o','p','q','r','s','u','v','w','y','z','@','$','&','*','=', '']
#if character is not in the list, let the user reenter it.
while character not in permitted:
    character = (input('Character not permitted! Try again: '))
   
print()
if ctype == "24":
    list_time = strToInt(time)
    if(len(list_time) == 3):   
   #adds the colon afther the first digit if there is only one number for the hour
        numbers(list_time[0],final)
        final[0].append(' ')
        final[1].append(':')
        final[2].append(' ')
        final[3].append(':')
        final[4].append(' ')
        numbers(list_time[1],final)
        numbers(list_time[2],final)
    elif(len(list_time) == 4):
        numbers(list_time[0],final)
        numbers(list_time[1],final)

        final[0].append(' ')
        final[1].append(':')
        final[2].append(' ')
        final[3].append(':')
        final[4].append(' ')
        numbers(list_time[2],final)
        numbers(list_time[3],final)
        
    if character != '':
        symbol_change(final, character)
        

    
elif ctype == "12":
    list_time = strToInt(time)
    
    if list_time[0] == 0:
        num_in_12 = '12'
        list_time_for_12 = [1,2,list_time[1], list_time[2]]
        numbers(list_time_for_12[0],final)
        numbers(list_time_for_12[1],final)

        final[0].append(' ')
        final[1].append(':')
        final[2].append(' ')
        final[3].append(':')
        final[4].append(' ')
        numbers(list_time_for_12[2],final)
        numbers(list_time_for_12[3],final)
        
    elif(len(list_time) == 3):   
   #adds the colon afther the first digit if there is only one number for the hour
        numbers(list_time[0],final)
        final[0].append(' ')
        final[1].append(':')
        final[2].append(' ')
        final[3].append(':')
        final[4].append(' ')
        numbers(list_time[1],final)
        numbers(list_time[2],final)
    elif(len(list_time) == 4):
        num = int(str(list_time[0]) + str(list_time[1]))  #gets the hour number
        if num >= 13:
            num_for_12 = str(num -12)
 
        
        
        list_time_for_12 =[]
        for i in num_for_12:
            list_time_for_12.append(int(i))
            
        
        list_time_for_12.append(list_time[2])
    

        list_time_for_12.append(list_time[3])
        

        
        if(len(list_time_for_12) == 3):   
       #adds the colon afther the first digit if there is only one number for the hour
            numbers(list_time_for_12[0],final)
            final[0].append(' ')
            final[1].append(':')
            final[2].append(' ')
            final[3].append(':')
            final[4].append(' ')
            numbers(list_time_for_12[1],final)
            numbers(list_time_for_12[2],final)
        elif(len(list_time_for_12) == 4):   
       #adds the colon afther the first digit if there is only one number for the hour
            numbers(list_time_for_12[0],final)
            numbers(list_time_for_12[1],final)

            final[0].append(' ')
            final[1].append(':')
            final[2].append(' ')
            final[3].append(':')
            final[4].append(' ')
            numbers(list_time_for_12[2],final)
            numbers(list_time_for_12[3],final)
     

    if character != '':
        symbol_change(final,character)
    
    #adds the pm/am after the symbols are changed
    AM_or_PM(list_time,final)
   
    
        
        

 
layout(final)

 
