#global variables

import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

currentPlayer = "X"
winner = None
gameRunning =True


#we need a game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input

def playerInput(board):
    inp = int(input("Please enter a value from 1 to 9 for positioning your piece_"))
    if inp <=9 and inp >= 1 and board[inp-1] == "_":
        board[inp-1] = currentPlayer
    else:
        print("Error input!")

#check for win or tie

def checkHorizontalWin(board):
    global winner
    if board[0] == board[1] == board[2] and board [0] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board [5] != "_":
        winner = board[5]
        return True
    elif board[6] == board[7] == board[8] and board [6] != "_":
        winner = board[0]
        return True
    
def checkVerticalWin(board):
    global winner
    if board[0] == board[3] == board[6] and board [0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board [1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board [2] != "_":
        winner = board[2]
        return True
    
def checkDiagonalWin(board):
    global winner
    if board[0] == board[4] == board[8] and board [0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board [2] != "_":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False
    
def checkWin(board):
    if checkVerticalWin(board) or checkDiagonalWin(board) or checkHorizontalWin(board):
        print(f"The winner is, {winner}")
        global gameRunning
        gameRunning = False

#switch the player
        
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#if playing against computer

def computerMove(board):
    global currentPlayer
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "_":
            board[position] = "O"
            switchPlayer()
    
    
    

#chech for the win or tie again
        
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computerMove(board)
    checkTie(board)
    checkWin(board)