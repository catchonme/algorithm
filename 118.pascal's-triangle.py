#!/usr/bin/python3


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(res[-1][j-1]+res[-1][j])
            tmp.append(1)
            res.append(tmp)
        return res


sol = Solution()
result = sol.generate(5)
print(result)