#!/usr/bin/python3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, start, n = 0, 0, len(s)
        maps = {}
        for i in range(n):
            start = max(start, maps.get(s[i], -1) + 1)
            l = max(l, i - start + 1)
            maps[s[i]] = i
        return l


sol = Solution()
res = sol.lengthOfLongestSubstring("pwwkew")
print(res)
