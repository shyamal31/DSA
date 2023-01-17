
# %%  
def greatestCommonFactor(a,b):
    x = max(a,b)
    y = min(a,b)
    while y!=0:
        x,y = y, x%y
    return x
    
def isGoodArray(nums):
    for i in range(1,len(nums)):
        if greatestCommonFactor(nums[0],nums[i]) == 1:
            return True
        else:
            return False
            
        
        
print(isGoodArray([3,6]))


