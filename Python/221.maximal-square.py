#!/usr/bin/python3


class Solution(object):
    def maximalSquare(self, matrix):
        dp = []
        for i in matrix:
            tmp = []
            for j in i:
                tmp.append(int(j))
            dp.append(tmp)

        row = len(dp)
        col = len(dp[0]) if row else 0

        for i in range(1, row):
            for j in range(1, col):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        maxv = 0
        for i in range(row):
            for j in range(col):
                if dp[i][j] > maxv:
                    maxv = dp[i][j]

        return maxv * maxv


matrixInput = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

sol = Solution()
res = sol.maximalSquare(matrixInput)
print(res)