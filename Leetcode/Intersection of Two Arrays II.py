class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        freq = {}
        
        for item in nums1:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
                
        for item1 in nums2:
            if item1 in freq:
                if freq[item1] > 0:
                    freq[item1] -= 1
                    result.append(item1)
                
        # for i in range(len(nums2)):
        #      if freq[nums2[i]] > 0:
        #         result.append(nums2[i])
        #         freq[nums2[i]] -= 1
                
        return result