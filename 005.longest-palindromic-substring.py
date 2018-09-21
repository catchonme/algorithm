#!/usr/bin/python3
# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        m, l, r = 0, 0, 0

        for i in range(n):
            # odd case
            for j in range(min(i + 1, n - i)):
                if s[i - j] != s[i + j]:
                    break
                if 2 * j + 1 > m:
                    m = 2 * j + 1
                    l = i - j
                    r = i + j

            if i + 1 < n and s[i] == s[i + 1]:
                for j in range(min(i + 1, n - i - 1)):
                    if s[i - j] != s[i + j + 1]:
                        break
                    if 2 * j + 2 > m:
                        m = 2 * j + 2
                        l = i - j
                        r = i + j + 1

        return s[l:r + 1]


sol = Solution()
end = sol.longestPalindrome("babad")
print(end)
