# import math
# from xml.dom import minidom
# class Solution:
#     def majorityElement(self, nums) -> int:
#         nums = sorted(nums)
#         count =1
#         ans = 0
#         e = len(nums)-1
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 count+=1
#             else:
#                 count =1

#             if count > math.floor(len(nums)/2):
#                 return nums[i]


# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         if len(nums) == 1:
#             return False
#         nums = sorted(nums)
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False


# class Solution:
#     def intersect(self, nums1, nums2):
#         isc = []
#         nums1 = sorted(nums1)
#         s = 0
#         e = len(nums2)-1
#         for i in nums1:
#             if self.binarySearch(nums2,s,e,i) != -1:
#                 isc.append(i)
#                 s = self.binarySearch(nums2,s,e,i)+1
#         return isc 
        
        
#     def binarySearch(self, nums,s,e, target):
#         nums = sorted(nums)
# #         s = 0
# #         e = len(nums)-1
        
#         while s<=e:
#             mid = s + (e-s)//2
            
#             if target < nums[mid]:
#                 e = mid-1
#             elif target > nums[mid]:
#                 s = mid +1
#             else:
#                 return mid
#         return -1

# arr1 = [54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41]
# arr2= [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]
 
# sol = Solution()
# print(sol.intersect(arr1,arr2))
# # print(sol.majorityElement([2,2,1,1,1,2,2]))
# # print(sol.containsDuplicate([2,14,18,22,22]))


# %%
# class Solution:
#     def largestPerimeter(self, nums) -> int:
#         nums =sorted(nums)
        
#         i = 0
#         l = len(nums)-1
#         mx_perimeter = 0
#         while(i<=l-2):
#             if nums[i]+nums[i+1] > nums[i+2]:
#                 mx_perimeter = nums[i]+nums[i+1]+nums[i+2]
#                 i+=1
#             else:
#                 i+=1
#         return mx_perimeter
# sol = Solution()
# print(sol.largestPerimeter([3,2,3,4]))
        
# class Solution:
#     def sortByBits(self, arr):
#         hashmap = {}
#         for i in range(len(arr)):
#             count = 0
#             a = arr[i]
#             if a == 0:
#                 count = 0
    
#             while a != 0 and a >=1:
#                 if a%2 == 1:
#                     count+=1
#                 a = a//2
#             hashmap[arr[i]]= count

#         sorted(list(hashmap.values()))    
#         return hashmap


# sol = Solution()
# print(sol.sortByBits([1,2,3,4,5,6,7,8]))        
                

# class Solution:
        
#     def frequencySort(self, nums):

#         hashmap = {}
        
#         for i in range(len(nums)):
#             if nums[i] not in hashmap:
#                 hashmap[nums[i]] =1
#             else:
#                 hashmap[nums[i]]+=1
        
#         hashmap = sorted(hashmap.items(), key =  lambda x:x[1], reverse = True)
        
#         return hashmap
# sol = Solution()
# print(sol.frequencySort([1,1,2,2,2,3]))

# class Solution:
#     def threeSum(self, nums): 
#         nums.sort()
#         ans = []
        
#         for i in range(len(nums)-1):
#             if i == 0 or (i>0 and nums[i]!= nums[i-1]):
#                 s = i+1
#                 e = len(nums)-1
#                 sm = -nums[i]
                
#                 while(s<e):
#                     if nums[s]+nums[e] == sm:
#                         ans.append([nums[i],nums[s],nums[e]])
                    
#                         while(s<e and nums[s] == nums[s+1]):
#                             s+=1
#                         while(s<e and nums[e] == nums[e-1]):
#                             e-=1
#                         s+=1
#                         e-=1
#                     elif nums[s] + nums[e] < sm:
#                         s+=1
#                     else:
#                         e-=1
#         return ans
        
                
# class Solution:
#     def threeSumClosest(self, nums, target: int) -> int:
#         nums.sort()
#         for i in range(len(nums)-2):
#             s = i+1
#             e =len(nums)-1
#             if s<e:
#                 mn_sum = target -(nums[i]+nums[s]+nums[e])
#             while(s<e):
#                 if nums[i] + nums[s] + nums[e] < target:
#                     if target - (nums[i] + nums[e] + nums[s]) <=mn_sum:
#                         mn_sum = target - (nums[i] + nums[s]+ nums[e])
#                     s+=1
                    
#                 elif nums[i] +nums[s] +nums[e] >target:
#                     if target - (nums[i] + nums[e] + nums[s]) <=mn_sum:
#                         mn_sum = target - (nums[i] + nums[s]+ nums[e])
#                     e-=1
#                 else:
#                     return target
#         return mn_sum-target            
        

# sol = Solution()
# print(sol.threeSumClosest([-1,2,1,-4],1))


# class Solution:
#     def merge(self, intervals):
#         intervals = sorted(intervals)
#         merge_int = []
#         i = 0
#         while i <=len(intervals)-1:
#             ans = intervals[i]
#             j = i+1
#             while j<=len(intervals)-1:
#                 if ans[1] >= intervals[j][0] and ans[1] <= intervals[j][1]:
#                     ans[1] = intervals[j][1]
#                     j+=1
#                 else:
#                     i =j
#                     break
#             merge_int.append(ans)
#             i = j
#         return merge_int

# sol = Solution()
# print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))

# class Solution:
#     def largestNumber(self, nums) -> str:
#         #using merge sort
#         ans = self.mergesort(nums)
#         string =''
#         for i in ans:
#             string +=f'i'
#         return string
    
#     def mergesort(self, nums):
#         mid = len(nums)//2
#         first_half = self.mergesort(nums[0:mid])
#         second_half = self.mergesort(nums[mid:len(nums)])
        
#         return self.merge(first_half,second_half)
        
#     def merge(self,fh,sh):
#         i = 0
#         j = 0
#         m = 0
#         merge = [0]*(len(fh) + len(sh))
        
#         while i <=len(fh)-1 and j<=len(sh)-1:
#             if fh[i]%10 > sh[j]%10:
#                 merge[m] = fh[i]
#                 i+=1
#             else:
#                 merge[m] = sh[j]
#                 j+=1
#             m+=1
#         while i<=len(fh)-1:
#             merge[m] = fh[i]
#             i+=1
#             m+=1
#         while j<=len(sh)-1:
#             merge[m] = sh[j]
#             j+=1
#             m+=1
#         return merge


# class Solution:
#     def largestNumber(self,nums) -> str:
#         #using merge sort
#         ans = self.insertion(nums)
#         # string =''
#         # for i in ans:
#         #     string +=f'{i}'
#         return ans
    
#     def insertion(self,nums):
#         n = len(nums)-1
#         for i in range(n):
#             for j in range(i+1,0,-1):
#                 if nums[j-1]%10 < nums[j]%10:
#                     nums[j-1] ,nums[j] = nums[j], nums[j-1]
#                 else:
#                     break
#         return nums

# sol = Solution()
# print(sol.largestNumber([3,30,34,5,9]))


# class Solution:
#     def sortSentence(self, s: str) -> str:
#         ls = []
#         word = ''
#         for i in range(len(s)):
#             if s[i] == ' ':
#                 ls.append(word)
#                 word=''
#             else:
#                 word+=s[i]
#             if i == len(s)-1:
#                 ls.append(word)
        
#         for i in range(len(ls)):
#             if int(ls[i][-1])-1 != i:
#                 curr_pos = int(ls[i][-1])-1
#                 ls[i],ls[curr_pos] = ls[curr_pos], ls[i]
        
#         return ls

# sol = Solution()
# print(sol.sortSentence("KTFkUVVrmYMSo2 wXlQraUqblfhCfDLK3 IfTuftYVualQ6 NhpQ5 HlRjClVtQrTFcwbx4 fi1"))


# class Solution:
#     def freqAlphabets(self, s: str) -> str:
        
#         hashmap = {}
        
#         for i in range(1,27):
#             if i<=9:
#                 hashmap[str(i)] =chr(i+96) 
#             else:
#                 hashmap[str(i)] =chr(i+96)
    
        
#         ans = ''
#         word=''
#         i = 0
#         while i<=len(s)-1:
#             if i<len(s)-2 and s[i+2] == '#':
#                 ans+=hashmap[s[i]+s[i+1]]
#                 i+=3
#             else:
#                 ans+= hashmap[s[i]]
#                 i+=1
#         return ans

# sol = Solution()
# print(sol.freqAlphabets("10#11#12"))

# class Solution:
#     def longestCommonPrefix(self, strs) -> str:
#         if len(strs)==0 or strs is None:
#             return ''
#         prefix = ''
#         index = 0
#         for c in strs[0]:
#             for i in range(1,len(strs)):
#                 if i>len(strs[i]) or c!=strs[i][index]:
#                     return prefix
#             prefix+=c
#             index+=1
#         return prefix


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
        
#         for i in range(len(s)):
#             if s[i] == '(' or s[i] == '[' or s[i] == '{':
#                 stack.append(s[i])
                
#             elif s[i] == ')' and stack[len(stack)-1] == '(':
#                 stack.pop()
#             elif s[i] == ']' and stack[len(stack)-1]=='[':
#                 stack.pop()
#             elif s[i] == '}' and stack[len(stack)-1] =='{':
#                 stack.pop()
#             else:
#                 return False
        
#         if len(stack) == 0:
#             return True
#         else:
#             return False
        
            
# sol = Solution()
# print(sol.isValid("()"))             
            
            
# class Solution:
#     def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
#         z_index = []
        
#         for i in range(len(s)):
#             if s[i]=='0':
#                 z_index.append(i)

#         ls = [0]
#         for i in ls:
#             for j in range(i + minJump, min(i+maxJump, len(s)-1)+1):
#                 if j in set(z_index):
#                     ls.append(j)
#         return ls[-1] == len(s)-1
        
    # def binarySearch(self,string,i, z_index,maxJump):
    #     s = 1
    #     e = len(z_index)-1
    #     target = min(i+maxJump, len(string)-1) 
    #     while(s<=e):
    #         mid = s + (e-s)//2
    #         if z_index[mid] < target:
    #             s = mid+1
    #         elif z_index[mid] > target:
    #             e = mid-1
    #         else:
    #             return z_index[mid]
    #     return z_index[e]

# sol = Solution()
# print(sol.canReach("01101110",2,3))        
        
#         for j in range(1,len(z_index)):
#             if i+minJump<=z_index[j] and z_index[j]<=min(i+maxJump, len(s)-1):
#                 i = z_index[j]
        
# class Solution:
#     def maximumRemovals(self, s: str, p: str, removable) -> int:
        
#         def check(m):
#             i = 0
#             j = 0
            
#             while i<len(s) and j<len(p):
#                 if i in set(removable[:m+1]):
#                     i+=1
#                     continue
#                 if s[i] == p[j]:
#                     i+=1
#                     j+=1
#                 else:
#                     i+=1
#             return j == len(p)
        
#         r = len(removable)-1
#         l = 0
#         res = 0
#         while l <= r:
#             mid = (l+r)//2
            
#             if check(mid):
#                 l = mid+1
#                 res = max(res,mid+1)
#             else:
#                 r = mid-1
#         return res
     
                
        

# sol = Solution()
# print(sol.maximumRemovals("abcab","abc",[0,1,2,3,4]))


# class Solution:
#     def canTransform(self, start: str, end: str) -> bool:
#             if start.count('X') != end.count('X'): 
#                 return False

#             n = len(start)
#             i = j = 0

#             while i < n and j < n: 
#                 if start[i] == 'X': 
#                     i += 1
#                     continue
#                 if end[j] == 'X':
#                     j += 1
#                     continue

#                 if start[i] != end[j]: return False
#                 if start[i] == 'L' and i < j: return False
#                 if start[i] == 'R' and i > j:  return False

#                 i += 1
#                 j += 1

#             return True
# sol = Solution()
# print(sol.canTransform("RXXLRXRXL","XRLXXRRLX"))

# class Solution:
#     def multiply(self, num1: str, num2: str):
#         #base conditions
#         if num1 == '0' or num2 == '0':
#             return 0
#         if num1 == '1':
#             return num2
#         if num2 == '1':
#             return num1
        
#         i = len(num1)-1
#         j = len(num2)-1
#         ans = [0]*(len(num1)+len(num2))
#         for i in range(len(num1)-1,-1,-1):
#             for j in range(len(num2)-1,-1,-1):
#                 product = int(num1[i])*int(num2[j])
#                 product+=ans[i+j+1]
#                 ans[i+j+1] = product%10
#                 ans[i+j] += product//10
#         return ans
# sol  = Solution()
# print(sol.multiply('123','456'))

# class Solution:
#     def calculate(self, s: str) -> int:
#         priority = {'/':4, '*':3,'+':2,'-':1}
#         stack1 = []
#         stack2 = []
#         s = s.replace(' ','')
#         print(len(s))
#         for i in range(len(s)):
#             if s[i] not in priority and s[i]!=' ':
#                 stack1.append(s[i])
#             else:
#                 if len(stack2) == 0:
#                     stack2.append(s[i])
#                     continue
#                 if priority[stack2[-1]] > priority[s[i]]:
#                     a = stack1.pop()
#                     b =stack1.pop()
#                     c = self.operation(int(a),int(b),stack2[-1])
#                     stack1.append(c)
#                 else:
#                     stack2.append(s[i])
#         print(stack1,stack2)
        
#         j = len(stack2)-1
#         ans = 0
#         while len(stack2):
#             ans = self.operation(int(stack1.pop()),int(stack1.pop()),stack2.pop())
#             stack1.append(ans)
            
#         return ans
            
#     def operation(self,a,b,substring):
#         if substring == '/':
#             return b//a
#         elif substring == '*':
#             return a*b
#         elif substring == '+':
#             return a+b
#         elif substring == '-':
#             return a-b
            
# sol = Solution()
# print(sol.calculate(" 4*  3-4+10 /2 "))              
                    
        
# class Solution:
#     def minimumLength(self, s: str) -> int:
#         ls = [x for x in s]
#         remove = []
        
#         # if ls[0]!-ls[-1]:
#         #     return False
#         while len(ls)!=0  and ls[0] == ls[-1]:
#             char = ls[0]
            
#         return len(ls)
# sol= Solution()
# print(sol.minimumLength("cabaabac"))   

# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         # count = 0
#         # diff =0
        
#         # i = 0
#         # j = 0
        
#         # while i < len(s) and j < len(t):
#         #     diff = abs(ord(t[j])- ord(s[i]))
#         #     if diff !=0 and diff<=maxCost:
#         #         maxCost -=diff
#         #         count+=1
#         #     i+=1
#         #     j+=1
#         # return count
#         i = 0
#         for j in range(len(s)):
#             maxCost -= abs(ord(s[j]) - ord(t[j]))
#             if maxCost < 0:
#                 maxCost += abs(ord(s[i]) - ord(t[i]))
#                 i += 1
#         return j - i + 1
# sol = Solution()
# print(sol.equalSubstring("jzmhzdq","rymuemg",17))
        
# class Solution:
#     def shiftingLetters(self, s: str, shifts) -> str:
#         ls = [x for x in s]
#         l = len(ls)
#         for i in range(len(ls)):
#             for j in range(sum(shifts[i:l])):
#                 ls[i] = self.shift(ls[i])
#         return ''.join(ls)
        
    
    
    
    
#     def shift(self,letter):
#         return chr((ord(letter)+1)%123)

# sol = Solution()
# print(sol.shiftingLetters("bad",[10,20,30]))

# class Solution:
#     def findKthBit(self, n: int, k: int) -> str:
#         st = '0'
        
#         for i in range(n-1):
#             st+='1'+self.reverse(self.invert(st))
#         return st[k-1]


        
    
#     def reverse(self,string):
#         reverse_string = ''
        
#         for i in range(len(string)):
#             reverse_string += string[len(string)-1-i]
#         return reverse_string
    
#     def invert(self,string):
#         invert_str = ''
#         for i in range(len(string)):
#             if string[i] == '1':
#                 invert_str+='0'
#             else:
#                 invert_str+='1'
#         return invert_str
# sol = Solution()
# print(sol.findKthBit(3,1))


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         i,j = 0,0
        
#         while i <len(s) and j < len(p):
#             if s[i] == p[j]:
#                 i+=1
#                 j+=1
#             elif p[j] == '*':
#                 valid = p[j-1]
#                 if valid == '.':
#                     i+=1
#                 while i<len(s) and s[i] == valid:
#                     i+=1
#                 j+=1
#             elif p[j] == '.':
#                 i+=1
#                 j+=1
#             else:
#                 j+=1
        
#         if i!=len(s) or j<=len(s):
#             return False
#         else:
#             return True
# sol = Solution()
# print(sol.isMatch("aaabb","c*a*b*"))
def makeLargestSpecial(S):
        count = i = 0
        res = []
        for j, v in enumerate(S):
            count = count + 1 if v=='1' else count - 1
            if count == 0:
                res.append('1' + makeLargestSpecial(S[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])
print(makeLargestSpecial("11011000"))