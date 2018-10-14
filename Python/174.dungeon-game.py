#!/usr/bin/python3


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [0 for i in range(n)]

        dp[n-1] = max(-dungeon[m-1][n-1] + 1, 1)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                tmp = []
                if i + 1 < m:
                    tmp.append(dp[j])
                if j + 1 < n:
                    tmp.append(dp[j+1])
                if tmp:
                    dp[j] = max(min(tmp) - dungeon[i][j], 1)

        return dp[0]

