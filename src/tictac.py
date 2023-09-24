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
    user_column = []
    com = []
    com_column = []
    win = False
    com_win = False
    for i in range(len(board)):
        for n in range(len(board)):
            if board[i][n] == 'O':
                user.append(i)
                user_column.append(n)
        else:
            if len(user) == 3:
                win = True
                break
            else:
                user = []
    i = 0
    column_counter = 0
    while i < 3:
        for n in user_column:
            if i ==  n:
                column_counter += 1
                if column_counter == 3:
                    win = True
                    break
        column_counter = 0
        i += 1
    dg_counter = 0
    for i in range(len(board)):
        if board[i][i] == 'O':
            dg_counter += 1
            if dg_counter == 3:
                win = True
                break
    
    dg_counter = 0
    for i in range(len(board)):
        if board[i][2-i] == 'O':
            dg_counter += 1
            if dg_counter == 3:
                win = True
                break  
    # computer move evaluation        
    for i in range(len(board)):
        for n in range(len(board)):
            if board[i][n] == 'X':
                com.append(i)
                com_column.append(n)
        else:
            if len(com) == 3:
                com_win = True
                print('row winning')
                break
            else:
                com = []
    i = 0
    column_counter = 0
    while i < 3:
        for n in com_column:
            if i ==  n:
                column_counter += 1
                if column_counter == 3:
                    com_win = True
                    break
        column_counter = 0
        i += 1
    dg_counter = 0
    for i in range(len(board)):
        if board[i][i] == 'X':
            dg_counter += 1
            if dg_counter == 3:
                com_win = True
                break
    
    dg_counter = 0
    for i in range(len(board)):
        if board[i][2-i] == 'X':
            dg_counter += 1
            if dg_counter == 3:
                com_win = True
                break  
    return win, com_win
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
            user_win, com_win = winning_move(user)
            # Why I cannot upack boolean value from a function
            if user_win and com_win == True:
                return print("Draw !!!")
            elif user_win == True and com_win == False:
                return print("You Win !!!")
            elif user_win == False and com_win == True:
                return print("You lose !!!")
            else:
                pass
start()
