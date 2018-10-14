#!/usr/bin/python3


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [(i >> 1) ^ i for i in range(pow(2, n))]
        return res


sol = Solution()
res = sol.grayCode(2)
print(res)