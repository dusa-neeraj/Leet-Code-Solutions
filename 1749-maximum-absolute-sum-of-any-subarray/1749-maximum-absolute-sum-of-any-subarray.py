class Solution:
    def maxAbsoluteSum(self, nums):
        max_curr = max_sum = 0
        min_curr = min_sum = 0

        for num in nums:
            max_curr = max(num, max_curr + num)
            max_sum = max(max_sum, max_curr)

            min_curr = min(num, min_curr + num)
            min_sum = min(min_sum, min_curr)

        return max(max_sum, abs(min_sum))