#!/usr/bin/python3


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.iso(s, t) and self.iso(t, s)

    def iso(self, s, t):
        """
        :type s:
        :type t:
        :rtype:
        """
        mapx = {}
        for i in range(len(s)):
            if s[i] not in mapx:
                mapx[s[i]] = t[i]
            elif s[i] in mapx:
                if t[i] != mapx[s[i]]:
                    return False
        return True


sol = Solution()
res = sol.isIsomorphic('paper', 'title')
print(res)