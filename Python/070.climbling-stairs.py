#!/usr/bin/python3


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = [1, 2, 3]
        if n < 4:
            return fib[n-1]
        for k in range(3, n+1):
            fib[2] = fib[0] + fib[1]
            fib[0], fib[1] = fib[1], fib[2]
        return fib[2]


sol = Solution()
res = sol.climbStairs(3)
print(res)