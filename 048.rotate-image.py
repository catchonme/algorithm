#!/usr/bin/python3


class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
        return A
        # A[:] = map(list, zip(*A[::-1]))


matrixInput = [
  [5, 1, 9, 2],
  [2, 4, 8, 4],
  [13, 3, 6, 1],
  [32, 1, 3, 1]
]
sol = Solution()
res = sol.rotate(matrixInput)
print(res)