#!/usr/bin/python3


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(s,[])
        return self.res


    def dfs(self, s, stringList):
        if len(s) == 0:
            self.res.append(stringList)
        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:],stringList + [s[:i]])

    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and self.isPalindrome(s[1:-1])



sol = Solution()
result = sol.isPalindrome('aab')
print(result)