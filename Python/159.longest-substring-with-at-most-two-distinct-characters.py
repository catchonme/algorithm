#!/usr/bin/python3


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {}
        begin, end, counter, length = 0, 0, 0, 0
        while end < len(s):
            maps[s[end]] = maps.get(s[end], 0) + 1
            if maps[s[end]] == 1:
                counter += 1
            end += 1
            while counter > 2:
                maps[s[begin]] -= 1
                if maps[s[begin]] == 0:
                    counter -= 1
                begin += 1
            length = max(length, end - begin)
        return length


sol = Solution()
result = sol.lengthOfLongestSubstringTwoDistinct('eceba')
print(result)
