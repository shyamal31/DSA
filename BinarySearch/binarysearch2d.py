#for the sorted rows and sorted columns we can apply binary search in the matrix

def searchMatrix(matrix, target):
    r = 0
    c = len(matrix) -1

    while (r < len(matrix) and c>=0):
        if matrix[r][c] == target:
            return [r,c]
        if matrix[r][c] < target:
            r+=1
        elif matrix[r][c] > target:
            c-=1
    return [-1,-1]

print(searchMatrix([[1,2,3],[1.5,2.5,3.5],[2,3,4]], 5))


# %%
#strickly sorted matrix : the last element of a row will be less than the first elemenent of the next row


def binarySearch(mat,row,cStart, cEnd, target):
    while(cStart <=cEnd):
        mid = cStart + (cEnd-cStart)//2

        if (mat[row][mid] == target):
            return [row,mid]
        if mat[row][mid] < target:
            cStart = mid +1
        else:
            cEnd = mid-1
    return [-1,-1]


def searchStricklySorted(mat, target):
    rows = len(mat)
    cols = len(mat[0])
    rStart = 0
    rEnd = rows-1
    cMid = cols//2
    if rows == 1:
        return binarySearch(mat,0,0,cols-1,target)
    #run the loop till 2 rows are reamining
    while(rStart < (rEnd-1)):
        mid = rStart + (rEnd -rStart)//2
        if mat[mid][cMid] == target:
            return [mid,cMid]
        if mat[mid][cMid] < target:
            rStart = mid
        else:
            rEnd = mid

    #binary search in 1st row
    firstrow = binarySearch(mat, rStart,0,cols-1,target)
    if firstrow!=[-1,-1]:
        return firstrow
    else:
        return binarySearch(mat,rStart+1,0,cols-2,target)
    
    #now we have 2 rows
    #check whether the target is in the columns of two rows
    # if mat[rStart][cMid] == target:
    #     return [rStart,cMid]
    # if mat[rStart+1][cMid] == target:
    #     return [rStart+1,cMid]
    
    #search in 1st half

mat = [[1,1]]
print(searchStricklySorted(mat,0))



# %%
