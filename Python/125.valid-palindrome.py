#!/usr/bin/python3


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = ''
        s = s.lower()

        for i in s:
            if '0' <= i <= '9' or 'a' <= i <= 'z':
                new += i
        return new == new[::-1]

sol = Solution()
result = sol.isPalindrome("A man, a plan, a canal: Panama")
print(result)