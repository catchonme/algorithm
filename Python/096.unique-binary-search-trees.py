#!/usr/bin/python3


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]
        for i in range(2, n+1):
            s = 0
            for k in range(i):
                s += dp[k]*dp[i-k-1]
            dp[i] = s
        return dp[-1]


sol = Solution()
res = sol.numTrees(3)
print(res)