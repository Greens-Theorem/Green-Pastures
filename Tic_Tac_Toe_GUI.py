#author Cowen Hames January 2021
#Version 1.0 This project is my attempt at converting my Java console-based version of Tic-Tac-Toe from 2020 to a GUI in Python
from tkinter import *
import random
#vars

human_score = 0
cpu_score = 0
board = [[0 for x in range(5)] for y in range(3)] 

#window

window = Tk()
window.title("Tic-Tac-Toe!")

#lb

list1=Listbox(window, height=6, width=20, bg = 'TEAL')
list1.grid(row=0, column=0, rowspan=6, columnspan=1 )

#sb

sb1 = Scrollbar(window)
sb1.grid(row=0, column=2, rowspan=6, columnspan=1, sticky=N+S+W)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#labels

l1 = Label(window, text="Enter a location (ie. A1) then press 'Move': ")
l1.grid(row=0, column=1)

#text entry

move_choice = StringVar()
e1 = Entry(window, textvariable=move_choice)
e1.grid(row=1, column=1)

#methods

#create a new board

def new_game():
    board[0][0] = 'A1'
    board[0][1] = '|'
    board[0][2] = 'A2'
    board[0][3] = '|'
    board[0][4] = 'A3'
    board[1][0] = 'A4'
    board[1][1] = '|'
    board[1][2] = 'A5'
    board[1][3] = '|'
    board[1][4] = 'A6'
    board[2][0] = 'A7'
    board[2][1] = '|'
    board[2][2] = 'A8'
    board[2][3] = '|'
    board[2][4] = 'A9'
    list1.insert(END, "-------------",board[0], board[1], board[2],"-------------")

#function to allow the player to choose a position

def player_move():
    if move_choice.get() == 'A1':
        if (board[0][0] == 'A1'):
            board[0][0] = 'X'
        pass

    elif move_choice.get() == 'A2':
        if (board[0][2] == 'A2'):
            board[0][2] = 'X'
        pass
    elif move_choice.get() == 'A3':
        if (board[0][4] == 'A3'):
            board[0][4] = 'X'
        pass
    elif move_choice.get() == 'A4':
        if (board[1][0] == 'A4'):
            board[1][0] = 'X'
        pass
    elif move_choice.get() == 'A5':
        if (board[1][2] == 'A5'):
            board[1][2] = 'X'
        pass
    elif move_choice.get() == 'A6':
        if (board[1][4] == 'A6'):
            board[1][4] = 'X'
        pass
    elif move_choice.get() == 'A7':
        if (board[2][0] == 'A7'):
            board[2][0] = 'X'
        pass
    elif move_choice.get() == 'A8':
        if (board[2][2] == 'A8'):
            board[2][2] = 'X'
        pass
    elif move_choice.get() == 'A9':
        if (board[2][4] == 'A9'):
            board[2][4] = 'X'
        pass
    else:
        Message("Enter a valid position!")

    computer_move()
    list1.insert(END, "------",board[0], board[1], board[2],"------")

    #call the end game methods in the event of a winner

    check_player_winner()
    check_cpu_winner()

#computer function to select a position

def computer_move():
    check1 = random.randint(0,2)
    check2 = random.randint(0,2)

    if (check1 == 0 and check2 == 0):
        if (board[0][0] == 'A1'):
            board[0][0] = 'O'
        pass
    elif (check1 == 0 and check2 == 1):
        if (board[0][2] == 'A2'):
            board[0][2] = 'O'
        pass
    elif (check1 == 0 and check2 == 2):
        if (board[0][4] == 'A3'):
            board[0][4] = 'O'
        pass
    elif (check1 == 1 and check2 == 0):
        if (board[1][0] == 'A4'):
            board[1][0] = 'O'
        pass

    elif (check1 == 1 and check2 == 1):
        if (board[1][2] == 'A5'):
            board[1][2] = 'O'
        pass

    elif (check1 == 1 and check2 == 2):
        if (board[1][4] == 'A6'):
            board[1][4] = 'O'
        pass

    elif (check1 == 2 and check2 == 0):
        if (board[2][0] == 'A7'):
            board[2][0] = 'O'
        pass

    elif (check1 == 2 and check2 == 1):
        if (board[2][2] == 'A8'):
            board[2][2] = 'O'
        pass

    elif (check1 == 2 and check2 == 2):
        if (board[2][4] == 'A9'):
            board[2][4] = 'O'
        pass

    list1.insert(END, "------",board[0], board[1], board[2],"------")

#check if the player won the game

def check_player_winner():

    if(board[0][0] == 'X' and board[0][2] == 'X' and board[0][4] == 'X'):
        won_game()
    elif(board[1][0] == 'X' and board[1][2] == 'X' and board[1][4] == 'X'):
        won_game()
    elif(board[2][0] == 'X' and board[2][2] == 'X' and board[2][4] == 'X'):
        won_game()

    #column winner

    elif(board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
        won_game()
    elif(board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        won_game()
    elif(board[0][4] == 'X' and board[1][4] == 'X' and board[2][4] == 'X'):
        won_game()

    #diagonal winner

    elif(board[0][0] == 'X' and board[1][2] == 'X' and board[2][4] == 'X'):
        won_game()
    elif(board[0][2] == 'X' and board[1][2] == 'X' and board[2][0] == 'X'):
        won_game()

#check if the computer won the game

def check_cpu_winner():

     #row winner

    if(board[0][0] == 'O' and board[0][2] == 'O' and board[0][4] == 'O'):
        lost_game()
    elif(board[1][0] == 'O' and board[1][2] == 'O' and board[1][4] == 'O'):
        lost_game()
    elif(board[2][0] == 'O' and board[2][2] == 'O' and board[2][4] == 'O'):
        lost_game()

    #column winner

    elif(board[0][0] == 'O' and board[1][0] =='O' and board[2][0] == 'O'):
        lost_game()
    elif(board[0][2] == 'O' and board[1][2] =='O' and board[2][2] == 'O'):
        lost_game()
    elif(board[0][4] =='O' and board[1][4] == 'O' and board[2][4] == 'O'):
        lost_game()

    #diagonal winner

    elif(board[0][0] == 'O' and board[1][2] =='O' and board[2][4] == 'O'):
        lost_game()
    elif(board[0][2] == 'O' and board[1][2] =='O' and board[2][0] == 'O'):
        lost_game()
    
#end game scenario #1

def won_game():
    list1.delete(0, END)
    global human_score
    human_score += 1
    list1.insert(0, "WINNER!", "Your Score: " + str(human_score), "Computer Score: " + str(cpu_score))

#end game scenario #2

def lost_game():
    list1.delete(0, END)
    global cpu_score
    cpu_score += 1
    list1.insert(0, "GAME OVER!", "Your Score: " + str(human_score), "Computer Score: " + str(cpu_score))

#buttons

b1 = Button(window, text = "New Game", width = 9, bg = 'TEAL', command = new_game)
b1.grid(row=3,column =1)

b2 = Button(window, text = "Move", width = 9, bg = 'TEAL', command = player_move)
b2.grid(row=2,column =1)

b3 = Button(window, text="Exit", width=9, bg = 'TEAL', command=window.destroy)
b3.grid(row=4, column=1)

#main

window.mainloop()