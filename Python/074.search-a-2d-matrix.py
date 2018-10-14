#!/usr/bin/python3


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        l, r = 0, row - 1
        while l <= r:
            mid_row = l + ((r - l) >> 2)
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                m, n = 0, col - 1
                while m <= n:
                    mid_col = m + ((n - m) >> 2)
                    if matrix[mid_row][mid_col] > target:
                        n = mid_col - 1
                    elif matrix[mid_row][mid_col] < target:
                        m = mid_col + 1
                    else:
                        return True
                return False
            elif target < matrix[mid_row][0]:
                r = mid_row - 1
            else:
                l = mid_row + 1
        return False


matrixInput = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
sol = Solution()
res = sol.searchMatrix(matrixInput, 23)
print(res)
