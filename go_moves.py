# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:41:10 2023

@author: raopr
"""

def initBoard():
    board = [["." for i in range(9)] for j in range(9)]
    return board

def printBoard(board):  
    for i in range(9):
        for j in range(9):
            print(board[i][j] + " ", end = "")
        print("\n")
        
def rowCol(place):
        place = place.split(",")
        row = int(place[0])-1
        col = int(place[1])-1
        return row, col

def check(row, col, board):
    if(row >= 9 or row < 0 or col >= 9 or col < 0):
        return 2
    elif(board[row][col] == "."):
        return 1
    return 3
    

board = initBoard()
printBoard(board)
players = [['White', 'O'], ['Black', '@']]
index = 1
while True:
    placeString = input(f"{players[index][0]}'s move. Type in (row, col) format or type 'stop': ")
    if (placeString == 'stop'):
        print('Stopping the game')
        break
    row, col = rowCol(placeString)
    proceed = check(row, col, board)
    if proceed == 1:
        board[row][col] = players[index][1]
        index = 1 - index
        printBoard(board)
    elif proceed == 2:
        print("Out of bounds of the board. Please try again")
    else:
        print("That spot is taken. Try again")
        
    
    
