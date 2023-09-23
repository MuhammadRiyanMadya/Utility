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
    global user_win, com_win
    user = []
    user_col= []
    com = []
    com_col = []
    user_win = False
    com_win = False
    counter = 0
    counter_com = 0
    

    for i, v in enumerate(board):
        if 'O' in v:
            user.append(i)
            user_col.append(v.index('O'))
            # debugging
            # print('user: ', user)
            # print('user_col: ', user_col)
        if 'X' in v:        
            com.append(i)
            com_col.append(v.index('X'))
            # debugging
            # print('com: ', com)
            # print('com_col: ', com_col)
    if len(user) == 3:
       for i in range(len(user)):
           if user[i] == user[0] or user_col[i] == user_col[0]:
               counter += 1
               if counter == 3:
                   user_win = True
                   return user_win
           elif i == user[i] and i == user_col[i]:
               counter += 1
               if counter == 3:
                   user_win = True
                   return user_win
           elif (user[i] + user_col[i] == 2):
               counter += 1
               if counter == 3:
                   user_win = True
                   return user_win
           else:
               user_win = False
       for i in range(len(com)):
           if com[i] == com[0] or com_col[i] == com_col[0]:
               counter_com += 1
               if counter_com == 3:
                   com_win = True
                   return com_win
           elif i == com[i] and i == com_col[i]:
               counter_com += 1
               if counter_com == 3:
                   com_win = True
                   return com_win
           elif (com[i] + com_col[i] == 2):
               counter_com += 1
               if counter_com == 3:
                   com_win = True
                   return com_win
           else:
               com_win = False
    return
          
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
            winning_move(user)
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
