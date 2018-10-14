#!/usr/bin/python3


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        self.res = []
        self.wordBreakLst("", s, wordDict)
        return self.res

    def wordBreakLst(self, lst, rest, wordDict):
        if rest == '':
            self.res.append(lst.rstrip())
        for i in range(1+len(rest)):
            if rest[:i] in wordDict:
                self.wordBreakLst(lst + rest[:i] + " ", rest[i:], wordDict)


sol = Solution()
result = sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print(result)