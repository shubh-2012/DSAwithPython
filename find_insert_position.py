

def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1
    mid = 0
    while (start <= end):
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if target > nums[mid]:
        return mid + 1
    else:
        return mid

nums = [1,2,4,5]
target = 3
ans = searchInsert(nums,target)
print(ans)