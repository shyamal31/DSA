#here we can move in any four direction in the maze to reach the final destination.
def mazebacktracking(p, maze,r,c):
    if r == len(maze)-1 and c == len(maze)-1:
        ls = []
        ls.append(p)
        return ls
    
    ls = []
    if not maze[r][c]:
        return ls
    maze[r][c] =False

    if r<len(maze)-1:
        ls.extend(mazebacktracking(p+'D',maze,r+1,c))
    
    if c< len(maze[0])-1:
        ls.extend(mazebacktracking(p+'R',maze,r,c+1))

    if r>0:
        ls.extend(mazebacktracking(p+'U',maze,r-1,c))
    if c>0:
        ls.extend(mazebacktracking(p+'L',maze,r,c-1))
    maze[r][c] =True
    return ls


def mazebacktrackingpath(p, maze,r,c,path,step):
    if r == len(maze)-1 and c == len(maze)-1:
        path[r][c] =step
        for a in path:
            print(a)
        print(p) 
        return 
    

    if not maze[r][c]:
        return 
    maze[r][c] =False
    path[r][c] = step

    if r<len(maze)-1:
        mazebacktrackingpath(p+'D',maze,r+1,c,path,step+1)
    
    if c< len(maze[0])-1:
        mazebacktrackingpath(p+'R',maze,r,c+1,path,step+1)

    if r>0:
        mazebacktrackingpath(p+'U',maze,r-1,c,path,step+1)
    if c>0:
        mazebacktrackingpath(p+'L',maze,r,c-1,path,step+1)
    maze[r][c] =True
    path[r][c] = 0

if __name__ == '__main__':
    maze = [[True,True,True],
    [True,True,True],
    [True,True,True]]
    path = [[0,0,0],
    [0,0,0],
    [0,0,0]]
    # print(mazebacktracking('',maze,0,0))
    mazebacktrackingpath('',maze,0,0,path,1)

    


