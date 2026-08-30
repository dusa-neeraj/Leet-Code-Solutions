class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        sums = sum(nums[:k])
        ans = float(sums) / k
        for i in range(k, n):
            sums = sums - nums[i-k] + nums[i]
            ans = max(ans, float(sums) / k)
        return ans