#!/usr/bin/python3


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        dp[0][0] = 1

        # init the first line
        for i in range(1,n+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[m][n] == 1 


sol = Solution()
res = sol.isMatch("aa", "*")
print(res)