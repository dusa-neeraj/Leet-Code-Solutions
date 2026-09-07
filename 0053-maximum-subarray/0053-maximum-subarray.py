class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        maximum = nums[0]

        for n in nums[1:]:
            current = max(n, current + n)
            maximum = max(maximum, current)

        return maximum