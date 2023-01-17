#google question

class Solution:
    def letterCombinations(self, digits: str):
        return self.helper('',digits)
    
    def helper(self,p,digits):
        hashmap= {'2': 'abc', '3': 'def',
                   '4': 'ghi', '5':'jkl','6':'mno',
                   '7':'pqrs', '8':'tuv','9':'wxyz'}
        
        if len(digits) == 0:
            ls = []
            ls.append(p)
            return ls
        
        ls = []
        digit = digits[0]             
        for c in hashmap[digit]:
            ch = c
            beforels = self.helper(p+ch,digits[1:])
            ls.extend(beforels)
        return ls


#amazon dice question: give all the possible combination we can form out of the given number
    def dice(self,p,target):
        if target == 0:
            ls = []
            ls.append(p)
            return ls
        
        ls = []
        for i in range(1,target+1):
            ls.extend(self.dice(p+str(i),target-i))
        return ls

class Solution:
    def combinationSum(self, candidates, target: int):
        ans = []
        ds = []
        self.combinations(0,candidates,target,ans,ds)
        return ans
    
    def combinations(self, index,candidates,target,ans,ls):
        if index == len(candidates):
            if target == 0:
                ans.append(ls.copy())
            return
        
        if candidates[index] <= target:
            ls.append(candidates[index])
            self.combinations(index,candidates,target-candidates[index],ans,ls)
            ls.pop(-1)
        
        self.combinations(index+1,candidates,target,ans,ls)
            
class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)
        
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]         
            
        
            
            
        
            
        
if __name__ == '__main__':
    sol = Solution()
    # print(sol.dice('',2))
    print(sol.findTargetSumWays([1,1,1,1,1],3))
