
class Solution(object):
    def maxDistance(self, position, m):
        position.sort()

        low = 1
        high = position[-1] - position[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            cows = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= mid:
                    cows += 1
                    last = position[i]

            if cows >= m:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans