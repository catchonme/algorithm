#!/usr/bin/python3

# 解析可以参考
# https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/022._generate_parentheses.md
class Solution(object):
    def generateParentheses(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.singleStr('', 0, 0, n)
        return self.res

    def singleStr(self, s, left, right, n):
        if left == n and right == n:
            self.res.append(s)
        if left < n:
            self.singleStr(s + '(', left + 1, right, n)
        if right < left:
            self.singleStr(s + ')', left, right + 1, n)


sol = Solution()
res = sol.generateParentheses(3)
print(res)
