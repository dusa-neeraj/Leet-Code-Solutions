class Solution:
    def findMaxLength(self, nums):
        prefix = 0
        max_length = 0
        
        mp = {0: -1}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix in mp:
                length = i - mp[prefix]
                max_length = max(max_length, length)
            else:
                mp[prefix] = i
        
        return max_length