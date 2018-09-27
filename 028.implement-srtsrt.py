#!/usr/bin/python3

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


sol = Solution()
res = sol.strStr('hello', 'll')
print(res)