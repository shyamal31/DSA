def bubble(arr):
    n = len(arr)-1
    for i in range(n):
        swapped = False
        for j in range(1,n-i+1):
            if arr[j-1]  > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
                swapped=True
        if swapped == False:
            print('already sorted array')
            break
    return arr
    
def selection(nums):
    n = len(nums)-1
    for i in range(n):
        mn = i
        for j in range(i,n+1):
            if nums[j] < nums[mn]:
                mn = j
        nums[i], nums[mn] = nums[mn], nums[i]
    return nums

def insertion(nums):
    n = len(nums)-1
    for i in range(n-1):
        for j in range(i+1,0,-1):
            if nums[j-1] > nums[j]:
                nums[j] ,nums[j-1] = nums[j-1], nums[j]
            else:
                break
def cyclic(nums):
    i = 0
    l = len(nums)-1
    while(i<=l):
        corr_pos = nums[i]-1 
        if nums[i] != nums[corr_pos]:
            
            nums[i],nums[corr_pos] = nums[corr_pos],nums[i]            
        else:
            i+=1
    return nums


# merger sorting
def mergeSort(nums):
    l = len(nums)
    if l == 1:
        return nums
    mid = l//2

    left = mergeSort(nums[0:mid])
    right = mergeSort(nums[mid:l])

    return merge(left,right)

def merge(first,second):
    res = [0]*(len(first)+len(second))
    i ,j,k =0,0,0

    while i <len(first) and j<len(second):
        if first[i] > second[j]:
            res[k] = second[j]
            j+=1
        else:
            res[k] = first[i]
            i+=1
        k+=1

    while i < len(first):
        res[k] = first[i]
        i+=1
        k+=1
    while j <len(second):
        res[k] =second[j]
        j+=1
        k+=1
    
    return res       

#quick sort

def quicksort(nums,low,hi):
    if low>=hi:
        return 
    s = low
    e = hi
    m = s+(e-s)//2
    pivot = nums[m]

    while s<=e:
        while nums[s]< pivot:
            s+=1
        while nums[e] > pivot:
            e -=1
        if s<=e:
            nums[s],nums[e] = nums[e],nums[s]
            s+=1
            e-=1
    quicksort(nums,low,e)
    quicksort(nums,s,hi)
    return nums
arr = [3,5,2,1,4]
print(quicksort(arr,0,len(arr)-1))


print(mergeSort([4,3,6,4,-8,0,2,16]))

# print(cyclic([4,3,2,7,8,2,3,1]))
print(cyclic([1,1]))


# print(bubble([1, 2, 3, 4, 5, 8]))
# print(selection([4,6,2,5,3,1]))
print(insertion([4,3,6,4,-8,0,2,16]))