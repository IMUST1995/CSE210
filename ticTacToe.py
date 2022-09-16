
def displayBoard(board):
    print(f'{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}')

def askTurn(letter):
    numberSelected = input(f"{letter}'s turn to choose a square (1-9): ")
    return int(numberSelected)
 
def writeInTheBoard(board, selected):
    if type(board[selected-1]) == int:
        board[selected-1] = 'x'
        return board
    else:
        print('yOU CANT CHOOSE AGAIN THAT SPOT')
    
def checkBoard(board):
    #checking rows
    if(board[0] == board[1] and board[1] == board[2]):
        displayBoard(board)
        print(f'player {board[0]} win')
    elif(board[3] == board[4] and board[4] == board[5]):
        displayBoard(board)
        print(f'player {board[3]} win')
    elif(board[6] == board[7] and board[7] == board[8]):
        displayBoard(board)
        print(f'player {board[6]} win')
    #checking columns
    elif(board[0] == board[3] and board[3] == board[6]):
        displayBoard(board)
        print(f'player {board[0]} win')
    elif(board[1] == board[4] and board[4] == board[5]):
        displayBoard(board)
        print(f'player {board[1]} win')
    elif(board[2] == board[5] and board[5] == board[8]):
        displayBoard(board)
        print(f'player {board[2]} win colmn 3')
    #checking diagonals:
    elif(board[0] == board[4] and board[4] == board[8]):
        displayBoard(board)
        print(f'player {board[0]} win')
    elif(board[2] == board[4] and board[4] == board[6]):
        displayBoard(board)
        print(f'player {board[2]} win colmn 3')
    else:
        displayBoard(board)

def main():
    board = [1,2,'x',4,5,'x',7,8,9]
    displayBoard(board)
    selected = askTurn('x')
    board = writeInTheBoard(board, selected) 
    checkBoard(board)
    """ selected = askTurn('x')
    board = writeInTheBoard(board, selected)
    displayBoard(board) """

    
#start
#check winner
    #check rows
    #check columns
    #check diagonals
    #check boards is full
    #else it's a tie
#next turn
#end message
main()