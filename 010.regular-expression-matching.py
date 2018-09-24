#!/usr/bin/python3

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def helper(s, i, p, j):
            if j == -1:
                return i == -1
            if i == -1:
                if p[j] != '*':
                    return False
                return helper(s, i, p, j - 2)
            if p[j] == '*':
                if p[j-1] == '.' or p[j-1] == s[i]:
                    if helper(s, i-1, p, j):
                        return True
                return helper(s, i, p, j-2)
            if p[j] == '.' or p[j] == s[i]:
                return helper(s, i-1, p, j-1)
            return False
        return helper(s, len(s)-1, p, len(p)-1)


sol = Solution()
res = sol.isMatch('mississippi', 'mis*is*p*.')
print(res)