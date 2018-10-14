#!/usr/bin/python3


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :return: int
        """
        # n total rows of triangle
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        elif n == 2:
            return min(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1])
        else:
            res = []
            for i in range(n):
                res.append(triangle[i])
            res[0] = [triangle[0][0]]
            res[1] = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]

        for i in range(2, n):
            for j in range(i+1):
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == i:
                    res[i][j] = res[i-1][-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]

        return min(res[-1])


triangleInput = [
     [2],
    [3, 4],
   [6, 5, 7],
  [4, 1, 8, 3]
]
sol = Solution()
result = sol.minimumTotal(triangleInput)
print(result)
