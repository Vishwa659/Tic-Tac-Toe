import random  # Importing random module for computer's move

# Initial board setup with 9 empty spots
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"  # X will start first
winner = None        # No winner yet
gameRunning = True   # Game is active

# Function to print the current board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))  # Take position input
    # Check if input is valid and the position is empty
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer  # Place the player's symbol
    else:
        print("Oops! Spot is already taken or invalid.")  # Show error

# Function to check horizontal win
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# Function to check vertical win
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# Function to check diagonal win
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# Function to check for tie (if no "-" left)
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

# Function to check if there is a win
def checkWin():
    global gameRunning
    if checkHorizontle(board) or checkRow(board) or checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

# Function to switch player after each turn
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Function for computer's move (random selection)
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)  # Random index from 0 to 8
        if board[position] == "-":  # Check if position is free
            board[position] = "O"  # Place O
            switchPlayer()         # Switch turn to player

# Main game loop
while gameRunning:
    printBoard(board)      # Show current board
    playerInput(board)     # Take player's input
    checkWin()             # Check if player won
    checkTie(board)        # Check if tie
    switchPlayer()         # Switch to computer
    computer(board)        # Let computer play
    checkWin()             # Check if computer won
    checkTie(board)        # Check if tie
