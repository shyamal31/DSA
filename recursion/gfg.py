# def sumtraingle(arr):
#     if len(arr) < 1:
#         return 
#     ls = []
#     for i in range(len(arr)-1):
#          ls.append(arr[i]+arr[i+1])
#     sumtraingle(ls)
#     print(arr)
# # sumtraingle([1,2,3,4,5])

# def min(arr,n):
#     if n == len(arr):
#         return arr[-1]
#     ele = arr[n]
#     comp = min(arr,n+1)
#     if ele<comp:
#         return ele
#     else:
#         return comp

# def max(arr,n):
#     if n == len(arr):
#         return arr[-1]
#     ele = arr[n]
#     comp = max(arr,n+1)
#     if ele>comp:
#         return ele
#     else:
#         return comp
# print(max([1,2,-5,3],0))
# print(min([1,2,-5,3],0))


# cook your dish here



# def newFib(a,b,n):
#     if n == 1:
#         return b
#     elif n == 0:
#         return a
#     elif n == 2:
#         return a^b
#     return newFib(a,b,n%3)

# print(newFib(93,35,86))

