import random
#Board
board = ["1" , "2" , "3",
         "4" , "5" ,  "6",
         "7" , "8" ,  "9"]
gamerunning = True
player = "X"
winner = None
switch = True
#printing board
def printboard (board) :
    print('--*---*--')
    print (board[0] + " | " + board[1] + " | " + board[2])
    print('--*---*--')
    print (board[3] + " | " + board[4] + " | " + board[5])
    print('--*---*--')
    print (board[6] + " | " + board[7] + " | " + board[8])
    print('--*---*--')
# Taking input
def playerinput (board) :
    inp = int(input("Choose a numer from 1-9 on the board : "))
    if inp >= 1 and inp <=9 and board[inp-1]  != "X" and board[inp-1]  != "O" :
        board[inp-1] = player
        switchplayer(False)
    else :
        print("Oops this position is already occupied")
        switchplayer(True)
# check for win or lose
def checkhorizontal (board) :
    global winner
    if board[0] == board [1] == board [2]:
        winner =  board[0]
        printboard(board)
        return True


    elif board[3] == board [4] == board [5]:
        winner =  board[3]
        printboard(board)
        return True
    elif board[6] == board [7] == board [8]:
        winner =  board[6]
        printboard(board)
        return True
def checkvertical (board):
    global winner
    if board[0] == board [3] == board [6]:
        winner =  board[0]
        printboard(board)
        return True
    elif board[1] == board [4] == board [7]:
        winner =  board[1]
        printboard(board)
        return True
    elif board[2] == board [5] == board [8]:
        winner =  board[2]
        return True
def checkdiagonal (board):
    global winner
    if board[0] == board [4] == board [8]:
        winner =  board[0]
        printboard(board)
        return True
    elif board[2] == board[4] == board[6]:
        winner = board[2]
        printboard(board)
        return True
def checktie (board):
    global gamerunning
    if "1" not in board and "2" not in board and "3" not in board and "4"not in board and "5" not in board and "6" not in board and "7"  not in board and "8" not in board and "9" not in board :
        printboard(board)
        print("It's a tie !")
        gamerunning = False
##switch players
def switchplayer(switch):
    global player
    if player == "X" and switch == True :
        player = "O"
        return player
    elif  player == "X" and switch == False :
        player = "X"
        return player
    elif player == "O" and switch == True :
        player = "X"
        return player
    elif  player == "O" and switch == False :
        player = "O"
        return player
def checkwin():
    global gamerunning
    if checkvertical(board) == True or checkdiagonal(board) == True or checkhorizontal(board) == True :
        print("The winner is " , winner )
        gamerunning = False

###Playing against computer
def computerturn(board) :
    while player == "O" :
        position = random.randint(0,8)
        if board[position] == "1" or board[position] == "2" or board[position] == "3" or board[position] == "4" or board[position] == "5" or board[position] == "6" or board[position] == "7" or board[position] == "8" or board[position] == "9" :
            board[position] = "O"
            switchplayer(True)



while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer(switch)
    computerturn(board)
    checkwin()
    checktie(board)




