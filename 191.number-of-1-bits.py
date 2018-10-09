#!/usr/bin/python3


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


sol = Solution()
res = sol.hammingWeight(3)
print(res)