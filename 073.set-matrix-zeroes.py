#!/usr/bin/python3


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead
        """
        def setZero(i, j):
            for m in range(col):
                matrix[i][m] = 0
            for n in range(row):
                matrix[n][j] = 0

        row = len(matrix)
        col = len(matrix[0]) if row else 0
        new_matrix = [matrix[i][:] for i in range(row)]

        for i in range(row):
            for j in range(col):
                if new_matrix[i][j] == 0:
                    setZero(i, j)


matrixInput = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5]
]
sol = Solution()
res = sol.setZeroes(matrixInput)
print(matrixInput)
