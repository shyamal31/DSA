#This question has been asked in Google Interview

'''Given an array nums which consists of non-negative integers and an integer m, 
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.'''

class Solution:
    def splitArray(self, nums, m) -> int:
        start = 0
        end = 0

        for i in range(len(nums)):
            if nums[i] > start:
                start = nums[i]
            end +=nums[i]

        #binary search
        while (start < end):
            #try for the middle of this two as the potential answer
            mid = start + (end-start)//2

            #calc how many pieces you can divide this in twith this max sum]
            sum =0
            pieces = 1
            for i in nums:
                if sum + i > mid:
                    #you cannot add this in this subarray. make new one
                    #say you add this num in new subarray, then sum = num
                    sum = i
                    pieces+=1
                else:
                    sum+=i
            
            if pieces > m:
                start = mid+1
            else:
                end = mid

        
        return end

s = Solution()

print(s.splitArray([7,2,5,10,8],2))