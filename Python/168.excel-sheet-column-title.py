#!/usr/bin/python3


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n:
            ans = chr(ord('A') + (n-1) % 26) + ans
            n = (n - 1) // 26
        return ans

sol = Solution()
res = sol.convertToTitle(28)
print(res)
