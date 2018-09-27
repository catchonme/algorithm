#!/usr/bin/python3
import collections

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if len(words) == 0 or len(s) < len(words) * len(words[0]):
            return res
        n, m, wl = len(s), len(words), len(words[0])
        maps, cur_map = {}, {}
        maps = collections.Counter(words)
        for i in range(wl):
            count, start, r = 0, i, i
            while r + wl <= n:
                string = s[r:r + wl]
                if string in maps:
                    cur_map[string] = cur_map.get(string, 0) + 1
                    if cur_map[string] <= maps[string]:
                        count += 1
                    while cur_map[string] > maps[string]:
                        tmp = s[start:start + wl]
                        cur_map[tmp] -= 1
                        start += wl
                        if cur_map[tmp] < maps[tmp]:
                            count -= 1
                    if count == m:
                        res.append(start)
                        tmp = s[start:start + wl]
                        cur_map[tmp] -= 1
                        start += wl
                        count -= 1
                else:
                    cur_map = {}
                    count = 0
                    start = r + wl
                r += wl
            cur_map = {}
        return res


sol = Solution()
res = sol.findSubstring("barfoothefoobarman", ["foo", "bar"])
print(res)
