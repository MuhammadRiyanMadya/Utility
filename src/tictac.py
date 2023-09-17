# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:52:34 2023

@author: MMR
"""

def display_board(df):
    # df is a list showing the box status
    # df depends on user and computer input to the list
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')
    print(('|'+' '*7)*3 +'|')
    print('|'+' '*3 + f'{df[0]}' + ' '*3 +'|'+' '*3 + f'{df[1]}' + ' '*3+'|'+' '*3 + f'{df[2]}' + ' '*3 +'|')
    print(('|'+' '*7)*3 +'|')
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')
    print(('|'+' '*7)*3 +'|')
    print('|'+' '*3 + f'{df[3]}' + ' '*3 +'|'+' '*3 + f'{df[4]}' + ' '*3+'|'+' '*3 + f'{df[5]}' + ' '*3 +'|')
    print(('|'+' '*7)*3 +'|')
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')
    print(('|'+' '*7)*3 +'|')
    print('|'+' '*3 + f'{df[6]}' + ' '*3 +'|'+' '*3 + f'{df[7]}' + ' '*3+'|'+' '*3 + f'{df[8]}' + ' '*3 +'|')
    print(('|'+' '*7)*3 +'|')
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+',end='')
def move()
    df = [1,2,3,4,5,6,7,8,9]
    start_display = display_board(df)
    while True:
        # computer input
        While True:
            com_in = randrange(9)
            for i in df:
                if com_in == i:
                    df[i-1] = com_in
                    break
        update_display = display_board(df)
        # user input
        user_in = int(input("Input your move: ")
        for i in df:
            if user_in == i:
                df[i-1] = com_in
        update_display = display_board(df)
