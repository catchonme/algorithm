#!/usr/bin/python3


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs:List[str]
        :rtype: List[List[str]]
        """
        mapx = {}
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            if tmp in mapx:
                mapx[tmp].append(i)
            else:
                mapx[tmp] = [i]
        return mapx.values()


sol = Solution()
res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)