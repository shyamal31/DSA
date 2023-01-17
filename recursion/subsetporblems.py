#permutations and combinations
#subset = non adjacent collection
#the pattern of taking some elements and removing some of it is the subset pattern

#1. create all the subsets of the array
def subseq(p,up):
        if len(up) == 0:
            print(p)
            return 
        ch = up[0]
        subseq(p,up[1:])
        subseq(p+ch, up[1:])

subseq('','abc')
def subsetReturn(p,up):
    if len(up) == 0:
        ls = []
        ls.append(p)
        return ls

    ch = up[0]
    left = subsetReturn(p,up[1:])
    right = subsetReturn(p+ch,up[1:])

    left.extend(right)
    return left

def subsetIter(arr):
    ls = [[]]
    for i in arr:
        n = len(ls)
        for j in range(n):
            internal = ls[j].copy()
            internal.append(i)
            ls.append(internal)
    return ls

def subsetIterDuplicate (arr):
    arr.sort()
    ls = [[]]
    s = 0
    e = 0
    for i in range(len(arr)):
        s = 0
        if i> 0 and arr[i] == arr[i-1]:
            s = e+1
        e = len(ls)-1
        n = len(ls)
        for j in range(s,n):
            internal = ls[j].copy()
            internal.append(arr[i])
            ls.append(internal)
    return ls

def permutation(p, up):
    if len(up) == 0:
        print(p)
        return 
    ch = up[0]
    for i in range(len(p)+1):
        f = p[0:i]
        l = p[i:len(p)]
        permutation(f+ch+l,up[1:])
if __name__ == "__main__":
    permutation('','abc')

    

    

