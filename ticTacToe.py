
#displaying board
def displayBoard(board):
    print(f'-----\n{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}\n-----')

#asking for a number which represents the square
def askSquare(letter):
    #what is the number?
    numberSelected = int(input(f"{letter}'s turn to choose a square (1-9): "))
    #is in range this number?
    numberInRange = validateNumberRange(numberSelected)
    #if yes returned it
    if numberInRange:
        numberSelected = int(numberSelected)-1
        return numberSelected
    #if not ask for the number again
    else:
        while numberInRange == False:
            numberSelected = int(input('Out of range, please insert a valid number (1-9): '))
            numberInRange = validateNumberRange(numberSelected)
            if numberInRange == True:
                return numberSelected -1
#function which validates and return a true or false for the input number from user
def validateNumberRange(numberSelected):
    if numberSelected > 0 and numberSelected < 10:
        return True
    else:
        return False
#change and return a number for the sign of the user
def writeInTheBoard(board, selected, letter):
    #if that space is uccupied for a letter it will ask for other number which space shoulb be available
    while type(board[selected]) != int:
        selected = int(input("That square was already chosen, try again, insert number (1-9): ")) -1
    else:
        board[selected] = letter
        return board
#function which receive the letter of the playes and the board to call other function and this constitute a turn
def turn(letter, board):
    squareSelected = askSquare(letter)
    board = writeInTheBoard(board, squareSelected, letter)
    displayBoard(board)
#a function which check if exist three times the same letter in a row, a column or a diagoal
def checkBoard(board):
    #checking rows
    if board[0] == board[1] and board[1] == board[2]:
        print(f'player "{board[0]}" win')
        return True
    elif board[3] == board[4] and board[4] == board[5]:
        print(f'player "{board[3]}" win')
        return True
    elif board[6] == board[7] and board[7] == board[8]:
        print(f'player "{board[6]}" win')
        return True
    #checking columns
    elif board[0] == board[3] and board[3] == board[6]:
        print(f'player "{board[0]}" win')
        return True
    elif board[1] == board[4] and board[4] == board[7]:
        print(f'player "{board[1]}" win')
        return True
    elif board[2] == board[5] and board[5] == board[8]:
        print(f'player "{board[2]}" win')
        return True
    #checking diagonals:
    elif board[0] == board[4] and board[4] == board[8]:
        print(f'player "{board[0]}" win')
        return True
    elif board[2] == board[4] and board[4] == board[6]:
        print(f'player "{board[2]}" win')
        return True
    #checking draw
    elif type(board[0]) == str and type(board[1]) == str and type(board[2]) == str and type(board[3]) == str and type(board[4]) == str and type(board[5]) == str and type(board[6]) == str and type(board[7]) == str and type(board[8]) == str:
        print(f"It's a draw")
        return True
    else:
        return False

def main():
    board = [1,2,3,4,5,6,7,8,9]
    turns = ['x','o','x','o','x','o','x','o','x']
    winner = False
    i = 0
    displayBoard(board)
    while i < 10 and winner == False:
        turn(turns[i], board)
        winner = checkBoard(board)
        i = i + 1

main()
#Author Zeir Braidi CSE 210.
#I am pleased to inform you that although it took me a long time, I am very happy with the result, at first I was afraid that I would not be able to complete the assignment, however I became passionate and the hours simply disappeared. Thank you very much. Kind regards Zeir Braidi