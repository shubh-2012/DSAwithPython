

def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
    place = {}

    for i in range(len(nums)):
        place[nums[i]] = i

    for j in range(len(operations)):
        nums[place[operations[j][0]]] = operations[j][1]
        place[operations[j][1]] = place[operations[j][0]]

    return nums

# You are given a 0-indexed array nums that consists of n distinct positive integers.
# Apply m operations to this array,
# where in the ith operation you replace the number operations[i][0]
# with operations[i][1].
#
# It is guaranteed that in the ith operation:
#
# operations[i][0] exists in nums.
# operations[i][1] does not exist in nums.
# Return the array obtained after applying all the operations.
#
#
#
# Example 1:
#
# Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
# Output: [3,2,7,1]
# Explanation: We perform the following operations on nums:
# - Replace the number 1 with 3. nums becomes [3,2,4,6].
# - Replace the number 4 with 7. nums becomes [3,2,7,6].
# - Replace the number 6 with 1. nums becomes [3,2,7,1].
# We return the final array [3,2,7,1].