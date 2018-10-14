#!/usr/bin/python3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1))
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[0])))


gridInput = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
sol = Solution()
res = sol.numIslands(gridInput)
print(res)