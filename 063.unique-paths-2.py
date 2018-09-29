#!/usr/bin/python3


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for i in range(col)] for j in range(row)]

        dp[0][0] = int(obstacleGrid[0][0] == 0)

        # first row
        for j in range(1, col):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]

        # first col
        for i in range(1, row):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row-1][col-1]


matrixInput = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]

sol = Solution()
res = sol.uniquePathsWithObstacles(matrixInput)
print(res)