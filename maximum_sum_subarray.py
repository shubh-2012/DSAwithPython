

def max_sum_subarry(nums):
    sum = 0
    i = 0
    max_sum = nums[0]
    while (i < len(nums)):
        if sum + nums[i] > 0:
            sum += nums[i]
            i += 1
            if sum > max_sum:
                max_sum = sum
        else:
            if nums[i] > max_sum:
                max_sum = nums[i]
            i += 1
            sum = 0

    return max_sum

nums = [-1,2,3,-4,2]
print(max_sum_subarry(nums))

