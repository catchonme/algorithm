#!/usr/bin/python3


class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        m, n = 0, col - 1
        while m < row and n >= 0:
            if matrix[m][n] < target:
                m += 1
            elif matrix[m][n] > target:
                n -= 1
            else:
                return True

        return False


matrixInput = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
sol = Solution()
res = sol.searchMatrix(matrixInput, 3)
print(res)