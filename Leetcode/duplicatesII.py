def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    freq = {}

    for i in range(len(nums)):

        if nums[i] in freq:

            if abs(freq[nums[i]] - i) <= k:
                return True
            else:
                freq[nums[i]] = i

        else:

            freq[nums[i]] = i

    return False