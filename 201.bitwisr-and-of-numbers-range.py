#!/usr/bin/python3


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.rangeBitwiseAnd(m, n & n-1) if m < n else n

sol = Solution()
res = sol.rangeBitwiseAnd(0, 1)
print(res)