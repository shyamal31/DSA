import numpy as np
def knight(board, row,col,knights):
    if knights == 0:
        display(board)
        print()
        return 1
    count = 0
    if row == len(board):
        return count

    if col == len(board):
        count+=knight(board,row+1,0,knights)
        return count

    if isSafe(board,row,col):
        board[row][col] = True
        count+=knight(board,row,col+1,knights-1)
        board[row][col] = False
    count+=knight(board,row,col+1,knights)
    return count
def display(board):
    for x in board:
        for i in x:
            if i:
                print('K ',end = ' ')
            else:
                print('_ ',end = ' ' )
        print()

def isSafe(board,row,col):
    if isValid(board,row-2,col+1):
        if board[row-2][col+1]:
            return False
        
    if isValid(board,row-2,col-1):
        if board[row-2][col-1]:
            return False
    if isValid(board,row-1,col+2):
        if board[row-1][col+2]:
            return False

    if isValid(board,row-1,col-2):
        if board[row-1][col-2]:
            return False
    return True

def isValid(board,row,col):
    try:
        if row>=0 and row<len(board) and col>=0 and col<len(board):
            return True
        return False
    except:
        print(row,col,board,end = ' ')

if __name__ == '__main__':
    n = 4
    shape =(n,n)
    board = np.full((n,n), dtype = bool, fill_value = False)
    print(knight(board,0,0,n))