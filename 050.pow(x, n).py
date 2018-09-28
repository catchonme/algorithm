#!/usr/bin/python3


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n & 1:  # n 为奇数
            return x * self.myPow(x*x, n>>1)
        else:
            return self.myPow(x*x, n>>1)


sol = Solution()
res = sol.myPow(4, 2)
print(res)