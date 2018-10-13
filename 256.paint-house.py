#!/usr/bin/python3


class Solution(object):
    def minCost(self, costs):
        m = len(costs)
        if m == 0:
            return 0
        elif m == 1:
            return min(costs[0][0], costs[0][1], costs[0][2])
        else:
            n = 3 if m else 0
            dp = [[0 for i in range(3)] for j in range(m)]
            dp[0] = costs[0]

            for i in range(1, m):
                dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][9]
                dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
                dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
            return min(dp[m-1][0], dp[m-1][1], dp[m-1][2])

