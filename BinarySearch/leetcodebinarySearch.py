# class Solution:
#     def mySqrt(self, x: int) -> int:
#         hash = {}
#         for i in range(1,10):
#             hash[i*i] = i
#         # for i in range(1,32769):
#         #     hash[i*i] = i
        
#         nums = list(hash.keys())
#         s = 0
#         e = len(nums)-1
        
#         while(s != e-1):
#             mid = s + (e-s)//2
#             if x < nums[mid]:
#                 e = mid
#             elif x > nums[mid]:
#                 s = mid
#             else:
#                 return hash[nums[mid]]
#         return hash[nums[s]]
# s = Solution()
# print(s.mySqrt(4))

# class Solution:
#     def fairCandySwap(self, aliceSizes, bobSizes):
#         alicecandies = 0
#         bobcandies = 0
#         for i in aliceSizes:
#             alicecandies+=i
#         for i in bobSizes:
#             bobcandies+=i

#         s = min(alicecandies,bobcandies)
#         e = max(alicecandies,bobcandies)
        
#         eqcandies = s + (e-s)//2
        
#         a = 0
#         b = 0
#         aliceSizes = sorted(aliceSizes)
#         bobSizes = sorted(bobSizes)
        
#         while(a<=len(aliceSizes)-1 and b<=len(bobSizes)-1):
#             if aliceSizes[a] + bobSizes[b] < eqcandies:
#                 if a < b:
#                     a+=1
#                 else:
#                     b+=1
#             else:
#                 return [aliceSizes[a], bobSizes[b]]
    
# sol = Solution()
# print(sol.fairCandySwap([1,2],[2,3]))

# class Solution:
#     def checkIfExist(self, arr) -> bool:
#         arr = sorted(arr)
#         i = 0
#         j = 1
#         l = len(arr)-1
#         while(i<=l and j<=l):
#             if arr[i]*2 > arr[j]:
#                 j+=1
#             elif arr[i]*2 < arr[j]:
#                 i+=1
#             else:
#                 return True
#         return False
# sol = Solution()
# print(sol.checkIfExist([10,2,5,3]))

# class Solution:
#     def singleNonDuplicate(self, nums) -> int:
#         s =0
#         e = len(nums)-1
        
#         while(s<e):
#             mid = s + (e-s)//2
            
#             if nums[mid-1] < nums[mid] < nums[mid+1]:
#                 return nums[mid]
            
#             if nums[mid] > nums[mid-1]:
#                 if mid%2==0:
#                     s = mid+2
#                 else:
#                     e = mid-1
#             elif nums[mid] == nums[mid-1]:
#                 if mid%2 ==0:
#                     e = mid-2
#                 else:
#                     s = mid+1
#         return nums[s]
# sol = Solution()
# print(sol.singleNonDuplicate([1,2,2,3,3,4,4,8,8]))


# class Solution:
#     def maxValue(self, n: int, index: int, maxSum: int) -> int:

#         s= 1
#         e = maxSum
#         length = n-1
#         r = length-index
#         l = index
#         while(s<=e):
            
#             mid = s + (e-s)//2
#             rs =0
#             ls= 0
#             sum = mid
#             m = mid-1
#             if m >= r: #for right part of the array
#                 rs = m*(m+1)/2 - ((m-r)*(m-r+1)/2)
#             else:
#                 rs = m*(m+1)/2 + (r-m) #add one in the space remaining
                
#             if m>= l: #for left part of the array
#                 ls = m*(m+1)/2 - ((m-l)*(m-l+1)/2)
#             else:
#                 ls = m*(m+1)/2 + (l-m) #add one in the space remaini        
    
#             sum+=ls+rs
        
#             if sum<=maxSum:
#                 res = mid
#                 s = mid+1
#             elif sum > maxSum:
#                 e = mid-1
#         return res
            
# sol = Solution()
# print(sol.maxValue(3,0,815094800))


# class Solution:
#     def searchMatrix(self, matrix, target: int) -> bool:
        
#         rows = len(matrix)
#         cols = len(matrix[0])
        
#         if rows == 1 and cols==1:
#             return matrix[0][0] == target
        
#         rStart = 0
#         rEnd = rows-1
#         cMid = cols//2
        
        
#         while(rEnd-rStart>=2):
#             mid = rStart + (rEnd-rStart)//2
#             if matrix[mid][cMid] == target:
#                 return True
#             if matrix[mid][cMid] > target:
#                 rEnd= mid
#             elif matrix[mid][cMid] < target:
#                 rStart = mid
        
#         #now we will search in 2 remaining rows
#         if self.binarySearch(matrix,rStart,0,cols-1,target):
#             return True
#         else:
#             return self.binarySearch(matrix,rEnd,0,cols-1,target)
        
#     def binarySearch(self,matrix,row, colstart, colend, target):
#         while colstart<=colend:
#             mid = colstart + (colend - colstart)//2
            
#             if target > matrix[row][mid]:
#                 colstart = mid+1
#             elif target< matrix[row][mid]:
#                 colend = mid-1
#             else:
#                 return True
#         return False
        
# sol = Solution()
# print(sol.searchMatrix([[1],[3],[5]],3))    

# class Solution:
#     def maxFrequency(self, nums, k: int) -> int:
#         s = 1
#         e = len(nums)
#         nums = sorted(nums)
#         ans =1
#         while(s<=e):
#             mid = s+ (e-s)//2

#             sum_of_element = 0
#             for i in range(e-mid):
#                 sum_of_element+=nums[i]
#             delta = mid*nums[mid-1] - sum_of_element
        
                    
#             # sum_of_element = 0
#             # for i in range(mid):
#             #     sum_of_element+=nums[i]

#             # delta = mid*nums[mid-1] - sum_of_element
#             if self.valid_subarray(nums,mid,k):
#                 ans = mid
#                 s = mid+1
#             else:
#                 e = mid-1
#         return ans
            
#     def valid_subarray(self,nums,freq,k):
#         s= 0
#         e = len(nums)-freq
        
#         while(s<=e):
#             mid = s+(e-s)//2
#             sum_of_element=0
#             for i in range(mid,mid+freq):
#                 sum_of_element+=nums[i]
#             delta = freq*nums[mid+freq-1] - sum_of_element
#             if delta > k:
#                 e = mid-1
#             elif delta<=k:
#                 return True
#         return False
                
# sol = Solution()
# arr = [9926,9960,10000,9992,9917,9986,9934,9985,9977,9950,9922,9913,9971,9978,9984,9959,9934,9948,9918,9916,9967,9965,9985,9977,9988,9983,9900,9945,9913,9966,9968,9986,9939,9914,9980,9957,9921,9927,9917,9972,9974,9953,9984,9912,9975,9920,9966,9932,9921,9904,9928,9959,9993,9937,9934,9974,9937,9964,9922,9963,9991,9930,9944,9930,9982,9980,9967,9904,9955,9947,9924,9973,9997,9950,9905,9924,9990,9947,9953,9924,9977,9938,9951,9982,9932,9926,9928,9912,9917,9929,9924,9921,9987,9910,9927,9921,9929,9937,9919,9995,9949,9953]
# print(sol.maxFrequency(arr,3044))

# ss = 0
# for i in range(82):
    
#     ss+=sorted(arr)[i]
# print(ss)
# print(ss- 82*sorted(arr)[81])

# print(sorted(arr))


# [9900, 9904, 9904, 9905, 9910, 9912, 9912, 9913, 9913, 9914, 9916, 9917, 9917, 9917, 9918, 9919, 9920, 9921, 9921, 9921, 9921, 9922, 9922,
#  9924, 9924, 9924, 9924, 9926, 9926, 9927, 9927, 9928, 9928, 9929, 9929, 9930, 9930, 9932, 9932, 9934, 9934, 9934, 9937, 9937, 9937, 9938,
# 9939, 9944, 9945, 9947, 9947, 9948, 9949, 9950, 9950, 9951, 9953, 9953, 9953, 9955, 9957, 9959, 9959, 9960, 9963, 9964, 9965, 9966, 9966,
# 9967, 9967, 9968, 9971, 9972, 9973, 9974, 9974, 9975, 9977, 9977, 9977, 9978, 9980, 9980, 9982, 9982, 9983, 9984, 9984, 9985, 9985, 9986,
# 9986, 9987, 9988, 9990, 9991, 9992, 9993, 9995, 9997, 10000]

            
            

# %%
def partition(weights,mx_weight,days):
    possible_days = 0
    sm =0
    for i in range(len(weights)):
        if i == len(weights)-1:
            possible_days+=1
        if sm+weights[i] <=mx_weight:
            sm+=weights[i]
        else:
            possible_days+=1
            sm= weights[i]
    return possible_days<=days
print(partition([1,2,3,4,5,6,7,8,9,10],15,5))
        
        
# %%
