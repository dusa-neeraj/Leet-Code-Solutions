class Solution:
    def maxProduct(self, nums):
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        for x in nums[1:]:
            old_max = curr_max

            curr_max = max(x, old_max * x, curr_min * x)
            curr_min = min(x, old_max * x, curr_min * x)

            ans = max(ans, curr_max)

        return ans