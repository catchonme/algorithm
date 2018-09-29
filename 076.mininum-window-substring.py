#!/usr/bin/python3

import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ''
        if s == '' or t == '':
            return ''
        maps = collections.Counter(t)
        counter = len(maps.keys())
        begin, end, head, length = 0, 0, 0, float('inf')
        while end < len(s):
            if s[end] in maps:
                maps[s[end]] -= 1
                if maps[s[end]] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                if s[begin] in maps:
                    maps[s[begin]] += 1
                    if maps[s[begin]] > 0:
                        counter += 1
                    if end - begin < length:
                        length = end - begin
                        head = begin
                begin += 1
        if length == float('inf'):
            return ''
        return s[head:head+length]


sol = Solution()
res = sol.minWindow('ADOBECODEBANC', 'ABC')
print(res)