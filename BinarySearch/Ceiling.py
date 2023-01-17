def Ceiling(nums, target):
    start = 0
    end = len(nums) - 1

    while(start <= end):
        mid = start +(end-start)//2

        if nums[mid] > target:
            end = mid -1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return nums[mid]
    return nums[start]

def Floor(nums, target):
    start = 0
    end = len(nums) - 1

    while(start <= end):
        mid = start +(end-start)//2

        if nums[mid] > target:
            end = mid -1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return nums[mid]
    return nums[end]

def smallestletter(letters, target):
    l = len(letters)
    start = 0
    end = len(letters) - 1

    while(start <= end):
        mid = start +(end-start)//2

        if letters[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return letters[start%l]       

print(smallestletter(['c','f','j'], 'j'))
# print(Ceiling([1,3,4,5,8,13,16,18], 9))

# print(Floor([1,3,4,5,8,13,16,18], 9))


