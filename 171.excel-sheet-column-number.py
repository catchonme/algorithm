#!/usr/bin/python3


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {}
        for i in range(65, 91):
            maps[chr(i)] = i - 64

        lst = list(s)
        lst.reverse()
        num = 0
        for idx, item in enumerate(lst):
            num += maps[item] * (26 ** idx)
        return num


sol = Solution()
res = sol.titleToNumber('AB')
print(res)
