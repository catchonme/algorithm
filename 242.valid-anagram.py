#!/usr/bin/python3

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


sol = Solution()
res = sol.isAnagram("anagram", "nagaram")
print(res)
