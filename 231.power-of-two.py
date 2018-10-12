#!/usr/bin/python3


class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isPowerOfTwo(n/2)
        return False


sol = Solution()
res = sol.isPowerOfTwo(16)
print(res)