#maze problem
#1. no of ways

def mazecount(r,c):
    if r == 1 or c ==1:
        return 1
    path1 = mazecount(r-1,c)
    path2 = mazecount(r,c-1)
    return path1+path2

#2. print total paths
def mazepaths(p,r,c):
    if r ==1 and c==1:
        ls = []
        ls.append(p)
        return ls
    ls =[]
    if r>1:
        patha = mazepaths(p+'D',r-1,c)
        ls.extend(patha)
    if c>1:
        pathb = mazepaths(p+'R',r,c-1)
        ls.extend(pathb)
    return ls

def mazepathsdiagonal(p,r,c):
    if r ==1 and c==1:
        ls = []
        ls.append(p)
        return ls
    ls =[]
    if r>1 and c>1:
        pathc = mazepathsdiagonal(p+'C',r-1,c-1)
        ls.extend(pathc)
    if r>1:
        patha = mazepathsdiagonal(p+'D',r-1,c)
        ls.extend(patha)
    if c>1:
        pathb = mazepathsdiagonal(p+'R',r,c-1)
        ls.extend(pathb)
    return ls

#maze with obstacles


def mazeob(p,r,c,maze):
    if r == len(maze)-1 and c == len(maze[0])-1:
        ls = []
        ls.append(p)
        return ls
    ls = []
    if not maze[r][c]:
        return ls
    if r< len(maze)-1:
        patha = mazeob(p+'D',r+1,c,maze)
        ls.extend(patha)

    if c< len(maze[0])-1:
        pathb = mazeob(p+'R',r,c+1,maze)
        ls.extend(pathb)
    return ls



                  

if __name__ == "__main__":
    # print(mazecount(3,3))
    # print(mazepaths('',3,3))
    # print(mazepathsdiagonal('',3,3))
    obstacles = [[True,True,True],
    [True,True,True],
    [False,True,True]]
    print(mazeob('',0,0,obstacles))



