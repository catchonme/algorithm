#!/usr/bin/python3


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0]) if row else 0
        dp = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
                elif i > 0 and j == 0:
                    dp[i][j] = sum([grid[k][0] for k in range(i+1)])
                elif i == 0 and j > 0:
                    dp[i][j] = sum([grid[0][k] for k in range(j+1)])
                else:
                    dp[i][j] = grid[0][0]

        return dp[-1][-1]


matrixInput = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
sol = Solution()
res = sol.minPathSum(matrixInput)
print(res)