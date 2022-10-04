
def move_zeroes(nums):
    i= 1
    j = 0

    while i < (len(nums)):
        if nums[j] == 0 and nums[i]!=0:
            nums[j] = nums[i]
            nums[i] = 0
            j+=1
        elif nums[j]!=0:
            j+=1
        i+=1

nums = [0,2,0,1,3,13,0,1]
move_zeroes(nums)
print(nums)
