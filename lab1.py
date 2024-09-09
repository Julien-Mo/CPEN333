# student name: Julien Mo
# student number: 44489698

# A command-line Tic-Tac-Toe game 
import random

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 

def init() -> None:
    """ prints the banner messages 
        and prints the intial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    # Blank Row
    print()
    # Top Row
    print(f"   {board[0]} | {board[1]} | {board[2]}    0 | 1 | 2")
    # Divider
    print(f"   --+---+--    --+---+--")
    # Middle Row
    print(f"   {board[3]} | {board[4]} | {board[5]}    3 | 4 | 5")
    # Divider
    print(f"   --+---+--    --+---+--")
    # Bottom Row
    print(f"   {board[6]} | {board[7]} | {board[8]}    6 | 7 | 8")
    # Blank Row
    print()

def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    isNextMoveValid = False
    # Repeat until valid move chosen
    while not isNextMoveValid:
        nextMove = input("Next move for X (state a valid cell num): ")
        # Reject move if not an integer
        if not nextMove.isdigit():
            isNextMoveValid = False
            print("Must be an integer")
        # Reject move if not in range of board
        elif int(nextMove) not in range(0, 9):
            isNextMoveValid = False
            print("Must enter a valid cell number")
        # Reject move if already played
        elif board[int(nextMove)] != " ":
            isNextMoveValid = False
            print("Must enter a valid cell number")
        # Accept move if all criteria pass
        else:
            isNextMoveValid = True
            print(f"You chose cell {int(nextMove)}")
    # Update board
    board[int(nextMove)] = "X"
    printBoard()

def computerNextMove() -> None:
    """ Computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """
    possibleMoves = []
    # Get all possible moves based on open spaces
    for possibleMove in range(len(board)):
        if board[possibleMove] == " ":
            possibleMoves.append(possibleMove)
    # Randomly choose the computer's next move
    nextMoveIndex = random.randint(0, len(possibleMoves) - 1)
    # Update board
    board[possibleMoves[nextMoveIndex]] = "O"
    print(f"Computer chose cell {int(possibleMoves[nextMoveIndex])}")
    printBoard()

def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
    columnStartIndexes = [0, 3, 6]
    rowStartIndexes = [0, 1, 2]
    # Check for win with three in a row horizontally
    for x in columnStartIndexes:
        if board[x + 0] == board[x + 1] == board[x + 2] == who:
            return True
    # Check for win with three in a row vertically
    for x in rowStartIndexes:
        if board[x + 0] == board[x + 3] == board[x + 6] == who:
            return True
    # Check for win with three in a row diagonally
    if board[0] == board[4] == board[8] == who:
        return True
    if board[2] == board[4] == board[6] == who:
        return True
    return False

def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """
    # Check if player or computer won
    if hasWon(who):
        if who == "X":
            print("You won! Thanks for playing.")
        if who == "O":
            print("You lost! Thanks for playing.")
        return True
    # Check if draw (no more valid moves)
    if not " " in board:
        print("A draw! Thanks for playing.")
        return True
    return False

if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate