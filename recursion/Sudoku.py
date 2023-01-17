class Solution:
    def isValidSudoku(self, board) -> bool:
        n = len(board)
        row =-1
        col= -1
        
        emptyLeft = True
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    row = i
                    col = j
                    emptyLeft = False
                    break
            if not emptyLeft:
                break
        
        if emptyLeft:
            return True
        
        #backtrack
        
        for num in range(1,10):
            if self.isSafe(board,row,col,str(num)):
                board[row][col] = str(num)
                if self.isValidSudoku(board):
                    return True
                else:
                    board[row][col] = '.'
                    
        return False
    
    def isSafe(self,board, row,col,num):
        #check for the row 
        for r in range(len(board)):
            if board[r][col] == num:
                return False
        #check for the number in the column
        
        for c in range(len(board)):
            if board[row][c] == num:
                return False
        
        sqrt = int(len(board)**(0.5))
        
        start = int(row - row%sqrt)
        end = int(col - col%sqrt)
        
        for i in range(start, start+sqrt):
            for j in range(end, end+sqrt):
                if board[i][j] == num:
                    return 
        return True
                    
    def display(self,board):
        for row in board:
            for num in row:
                print(num, end = ' ')
            print()
                

if __name__ == '__main__':
    sol = Solution()
    board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    if sol.isValidSudoku(board):
        sol.display(board)
    else:
        print('cannot solve')

