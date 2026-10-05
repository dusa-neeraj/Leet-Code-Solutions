
class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num <= mid:
                    current_sum += num
                else:
                    subarrays += 1
                    current_sum = num

            if subarrays > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans