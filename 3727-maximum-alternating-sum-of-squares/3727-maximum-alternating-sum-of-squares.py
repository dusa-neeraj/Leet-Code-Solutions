
class Solution(object):
    def maxAlternatingSum(self, nums):
        nums.sort(key=lambda x: x * x, reverse=True)

        ans = 0

        for i in range(len(nums)):
            if i < (len(nums) + 1) // 2:
                ans += nums[i] * nums[i]
            else:
                ans -= nums[i] * nums[i]

        return ans
