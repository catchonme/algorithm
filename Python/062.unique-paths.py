#!/usr/bin/python3


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        dp = [0] * n
        dp[0] = 1
        for i in range(0, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]


sol = Solution()
res = sol.uniquePaths(7, 3)
print(res)