#!/usr/bin/python3


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split()
        res = " ".join(tmp[::-1])
        return res


sol = Solution()
result = sol.reverseWords('jack is my name')
print(result)