#!/usr/bin/python3


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        v1 = [int(x) for x in v1]
        v2 = [int(x) for x in v2]

        len1 = len(v1)
        len2 = len(v2)
        lenMax = max(len1, len2)
        for x in range(lenMax):
            v1Token = 0
            if x < len1:
                v1Token = v1[x]
            v2Token = 0
            if x < len2:
                v2Token = v2[x]
            if v1Token > v2Token:
                return 1
            elif v1Token < v2Token:
                return -1
        return 0


sol = Solution()
res = sol.compareVersion('-1', '1')
print(res)