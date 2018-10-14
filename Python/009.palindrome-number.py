#!/usr/bin/python3


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x != int(str(x)[::1]):
            return False
        else:
            return True


sol = Solution()
res = sol.isPalindrome(121)
print(res)