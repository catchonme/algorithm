#!/usr/bin/python3


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        return sum([max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1)])


sol = Solution()
result = sol.maxProfit([7,1,5,3,6,4])
print(result)