import numpy as np
def queen(board, row):
    if row == len(board):
        print('---------------------------------')
        display(board)
        
        return 1

    count =0
    for col in range(len(board)):
        if isSafe(board,row,col):
            board[row][col] = True
            count+= queen(board,row+1)
            board[row][col] = False
    return count

def isSafe(board,row,col):
    for i in range(0,row):
        if board[i][col]:
            return False
        
    left = min(row,col)
    for i in range(1,left+1):
        if board[row-i][col-i]:
            return False

    right = min(row,len(board)-1-col)
    for i in range(1,right+1):
        if board[row-i][col+i]:
            return False
    return True

def display(board):
    for x in board:
        for i in x:
            if i:
                print('Q ',end = ' ')
            else:
                print('_',end = ' ' )
        print()
if __name__ == '__main__':
    
    n = 4
    shape= (n,n)
    board  = np.empty(shape,dtype=bool)
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] =False
    print(board)
    print(queen(board,0))
    

    #time complexity = n*T(n-1) + O(n**2) => by solving this using akrabazi formula we will ge 