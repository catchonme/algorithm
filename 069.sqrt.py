#!/usr/bin/python3


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 1.0
        while abs(res*res-x) > 0.1:
            res = (res + x / res) / 2
        return int(res)


sol = Solution()
output = sol.mySqrt(8)
print(output)