#!/usr/bin/python3


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, res = 5, 0
        while n >= base:
            res += n // base
            base *= 5
        return res


sol = Solution()
result = sol.trailingZeroes(5)
print(result)