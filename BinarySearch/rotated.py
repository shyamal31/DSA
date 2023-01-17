# class Solution:
#     def search(self, nums, target):
#         pivot_element = self.pivot(nums)
#         l = len(nums) - 1
#         if pivot_element == -1:
#             return self.binarySearch(target,nums,0,l)
#         first_half = self.binarySearch(target,nums,0,pivot_element)
        
#         if first_half != -1:
#             return first_half
#         else:
#             return self.binarySearch(target,nums,pivot_element+1,l) 
        

        
#     def binarySearch(self,target,nums, s, e):
#         while (s<=e):
#             mid = s + (e-s)//2
#             if nums[mid] >target:
#                 e = mid - 1
#             elif nums[mid] < target:
#                 s = mid+1
#             else:
#                 return mid
#         return -1
            

        
    
#     def pivot(self,nums):
        
#         s =0 
#         e = len(nums)-1
        
#         while(s<=e):
#             mid = s + (e-s)//2
#             #4 cases to find the pivot element
            
#             if mid < e and nums[mid] > nums[mid+1]:
#                 return mid
#             if mid > s and nums[mid] < nums[mid-1]:
#                 return mid-1
            
#             if nums[mid] <= nums[s]:
#                 e = mid - 1
#             else:
#                 s = mid+1
#         return -1

class Solution:
    def search(self, nums, target):
        pivot_element = self.pivot(nums)
        l = len(nums) - 1
        if pivot_element == -1:
            return self.binarySearch(target,nums,0,l)
        first_half = self.binarySearch(target,nums,0,pivot_element)
        
        if first_half:
            return first_half
        else:
            return self.binarySearch(target,nums,pivot_element+1,l) 
        

        
    def binarySearch(self,target,nums, s, e):
        while (s<=e):
            mid = s + (e-s)//2
            if nums[mid] >target:
                e = mid - 1
            elif nums[mid] < target:
                s = mid+1
            else:
                return True
        return False
    
    def pivot(self,nums) ->int:
        
        s =0 
        e = len(nums)-1
        
        while(s<=e):
            mid = s + (e-s)//2
            #4 cases to find the pivot element
            
            if mid < e and nums[mid] > nums[mid+1]:
                return mid
            if mid > s and nums[mid] < nums[mid-1]:
                return mid-1
            
            if nums[s] == nums[mid] and nums[e] == nums[mid]:
                #remove the duplicates
                #before removing check if the start and end are pivots
                if (nums[s] > nums[s+1]) :
                    return s
                
                if (nums[e] < nums[e-1]):
                    return e-1
                s+=1
                e-=1
            
            elif(nums[s] < nums[mid] or (nums[mid] == nums[s] and nums[mid] > nums[e])):
                s = mid+1
            else:
                e = mid -1
        return -1
        return -1
            
            
        
        
s=  Solution()

print(s.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2))
            
            
        