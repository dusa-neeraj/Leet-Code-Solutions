class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)
        satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]

        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        for i in range(minutes, n):
            if grumpy[i] == 1:
                extra += customers[i]

            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            max_extra = max(max_extra, extra)

        return satisfied + max_extra