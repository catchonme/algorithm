#!/usr/bin/python3


class Solution(object):
    def maxProfix(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        opt = [0] * len(prices)
        for i in range(1, len(prices)):
            opt[i] = max(opt[i-1]+prices[i]-prices[i-1], 0)
        return max(opt)


sol = Solution()
result = sol.maxProfix([7, 1, 5, 3, 6, 4])
print(result)