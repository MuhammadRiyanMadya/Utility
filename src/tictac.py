# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:52:34 2023

@author: MMR
"""
from random import randrange

def display_board(board):
    # df is a list showing the box status
    # df depends on user and computer input to the list
    
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')
    print(('|'+' '*7)*3 +'|')
    print('|'+' '*3 + f'{board[0][0]}' + ' '*3 +'|'+' '*3 + f'{board[0][1]}' + ' '*3+'|'+' '*3 + f'{board[0][2]}' + ' '*3 +'|')
    print(('|'+' '*7)*3 +'|')
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')
    print(('|'+' '*7)*3 +'|')
    print('|'+' '*3 + f'{board[1][0]}' + ' '*3 +'|'+' '*3 + f'{board[1][1]}' + ' '*3+'|'+' '*3 + f'{board[1][2]}' + ' '*3 +'|')
    print(('|'+' '*7)*3 +'|')
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')
    print(('|'+' '*7)*3 +'|')
    print('|'+' '*3 + f'{board[2][0]}' + ' '*3 +'|'+' '*3 + f'{board[2][1]}' + ' '*3+'|'+' '*3 + f'{board[2][2]}' + ' '*3 +'|')
    print(('|'+' '*7)*3 +'|')
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')
    return board

def user_move(board):
    user_in = int(input("Input your move: "))
    for i in range(len(board)):
        for j in range(len(board)): 
            if user_in == board[i][j]:
                board[i][j] = 'O'
    user_update_display = display_board(board)
    return user_update_display

def computer_move(board):
    com_update_display = board
    while True:
        com_in = randrange(9)
        loop = False
        for i in range(len(com_update_display)):
            for j in range(len(com_update_display)):
                if com_in == com_update_display[i][j]:
                    com_update_display[i][j] = 'X'
                    loop = True
                    break                    
        if loop == True:
            break
    com_update_display = display_board(com_update_display)
    return com_update_display
    
def winning_move(board):
    user = []
    user_col = []
    com = []
    com_col = []
    for i,v in enumerate(board):
       if 'O' in v:        
          user.append(i)
          user_col.append(v.index('O'))
          if len(user) == 3 or len(user_col) == 3:
             return print("You Win The Game !!")
       if 'X' in v:        
          com.append(i)
          com_col.append(v.index('X'))
          if len(com) == 3 or len(com_col) == 3:
             return print("Sorry You Are Loose !!")

def start():
    init = True
    while True:
        if init == True:
            board = [['0' for i in range(0,3)] for j in range(0,3)]
            counter = 1
            for i in range(0,3):
                for j in range(0,3):
                    board[i][j] = counter
                    counter += 1
            board = display_board(board)
            user = user_move(board)
            init = False
        else:
            com = computer_move(user)
            user = user_move(com)
            result = winning_move(user)
            if 
