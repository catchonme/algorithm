#!/usr/bin/python3


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                left = i - 1 - dp[i-1]
                if left >= 0 and s[left] == '(':
                    dp[i] = dp[i-1] + 2
                    if left > 0:  # 判断left前面是否能与后面连起来
                        dp[i] += dp[left-1]
        return max(dp)


sol = Solution()
res = sol.longestValidParentheses("(()")
print(res)