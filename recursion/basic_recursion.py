def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

print(fact(3))

def sum_number(num):
    if num == 0:
        return 0
    return (num)%10 + sum_number(num//10)
print(sum_number(1923))

import math
def reverse_number(num):
    digits = int(math.log10(num)) + 1
    return helper(num,digits)
def helper(num, digits):
    if num%10 == num:
        return num
    rem = num%10
    return rem*int(math.pow(10,digits-1)) + helper(num//10, digits-1)
print(reverse_number(1903))

def palindrom(num):
    return num == reverse_number(num)
print(palindrom(1232))

def count_zero(n):
    return helper(n,0)

def helper(n,c):
    if n == 0:
        return c
    res = n%10
    if res == 0:
        return helper(n//10,c+1)
    else:
        return helper(n//10,c)

print(count_zero(100200))

#check sorted array
def sortedArray(arr,index):
    if index == len(arr)-1:
        return True
    return arr[index] < arr[index+1] and sortedArray(arr,index+1)
print(sortedArray([1,2,3,44,5],0)) 

#Linear serach

def lensearch(arr, index,target):
    if arr[index] == target:
        return index
    if index == len(arr)-1:
        return -1
    return lensearch(arr,index+1,target)
print(lensearch([32,1,18,9],0,10))

#linear search on multiple occurence
ans = []
def findAllIndex(arr,target,index):
    if index == len(arr):
        return -1
    if arr[index] == target:
        ans.append(index)
    findAllIndex(arr,target,index+1)
findAllIndex([1,0,3,1,0,12,1,0], 0, 0)
print(ans)

linear search without global variable and additional argument

def findAllIndex(arr,target,index):
    ans  = []
    if index == len(arr):
        return ans
    if arr[index] == target:
        ans.append(index)
    ansbefore = findAllIndex(arr,target,index+1)
    ans.extend(ansbefore)
    return ans

print(findAllIndex([1,2,3,1,4,1,5,1],1,0))

#rotated binary search

def rotatedbs(arr,target,s,e):
    if s > e:
        return -1
    m = s + (e-s)//2

    if arr[m] == target:
        return m
    
    if arr[s]<=arr[m]:
        if arr[s] <=target<=arr[m]:
            return rotatedbs(arr,target, s,m-1)
        else:
            return rotatedbs(arr,target,m+1,e)
    
    if target >=arr[m] and target<=arr[e]:
        return rotatedbs(arr,target,m+1,e)
    return rotatedbs(arr,target,s,m-1)
arr = [5,6,7,8,9,1,2,3]
print(rotatedbs(arr,11,0,len(arr)-1))


#Bubble Sort

def bubblesort(arr, i,j):
    if i == 0:
        return 
    if i>j:
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j] 
        
        bubblesort(arr,i,j+1)
    else:
        bubblesort(arr,i-1,0)
arr = [55,23,34,12,561,1,4]
bubblesort(arr,len(arr)-1, 0)
print(arr)

def selectionsort(arr, r,c,max):
    #base condition
    if r== 0:
        return 


    if r >= c:
        if arr[c] > arr[max]:
            selectionsort(arr,r,c+1,c)
        else:
            selectionsort(arr,r,c+1,max)

    else:
        arr[r],arr[max] = arr[max],arr[r]
        selectionsort(arr,r-1,0,0)
    
arr1 =  [2,3,4,1,5]
selectionsort(arr1,len(arr1)-1,0,0)
print(arr1)
     
    
def mergesort(arr,s,e):
    if e-s ==1:
        return
    m = s + (e-s)//2
    mergesort(arr,s,m)
    mergesort(arr,m,e)
    return merge(arr,s,m,e)

def merge(arr,s,m,e):
    mix = [0]*(e-s)    
    i = s
    j = m
    k = 0
    while i<m and j<e:
        if arr[i] < arr[j]:
            mix[k] = arr[i]
            i+=1
        else:
            mix[k] = arr[j]
            j+=1
        k+=1
    while i<m:
        mix[k]= arr[i]
        i+=1
        k+=1
    while j<e:
        mix[k] =arr[j]
        j+=1
        k+=1
    
    for l in range(len(mix)):
        arr[s+l] = mix[l]

arr = [2,33,1,5]
mergesort(arr,0,len(arr))
print(arr)

Quick Sort with recursion



def qsort(nums, l,h):
    if l>=h:
        return 
    s = l
    e = h
    m = s+ (e-s)//2
    pivot = nums[m]
    while s<=e:
        while nums[s] < pivot:
            s+=1
        while nums[e]>pivot:
            e-=1
        if s<=e:
            nums[s],nums[e] = nums[e],nums[s]
            s+=1
            e-=1
    qsort(nums,l,e)
    qsort(nums,s,h)
nums = [5,2,1,6,3,4]
qsort(nums,0,len(nums)-1)
print(nums)

def insertion(arr,n):
    if n<=1:
        return 
    
    insertion(arr,n-1)

    j = n-1
    while j>=0:
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
        else:
            break

arr = [1,3,2,5,4,6]
insertion(arr,len(arr))
print(arr)

def removeduplicates(expr):
    if len(expr) == 1:
        return expr
    
    if expr[0] == expr[1]:
        new_expr = expr[1:]
        return removeduplicates(new_expr)
    else:
        return expr[0] + removeduplicates(expr[1:])

print(removeduplicates('aabccba')) 


    