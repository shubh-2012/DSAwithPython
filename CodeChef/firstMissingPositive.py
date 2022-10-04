class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        list_freq = [0]*(len(nums)+1)
        
        for i in range(0,len(nums)):
            if nums[i]>=0 and nums[i]< len(nums)+1:
                list_freq[nums[i]] = nums[i]
       
            
        print(list_freq)
        
         
        for i in range(0,len(list_freq)):
            if list_freq[i] != i:
                return i
        return i+1
        
