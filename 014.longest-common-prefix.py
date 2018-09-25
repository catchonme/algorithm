#!/usr/bin/python3


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        dp = [strs[0]] * len(strs)
        for i in range(1, len(strs)):
            while not strs[i].startswith(dp[i - 1]):
                dp[i - 1] = dp[i - 1][:-1]
            dp[i] = dp[i - 1]
        return dp[-1]


sol = Solution()
res = sol.longestCommonPrefix(['laa', 'lab', 'lac'])
print(res)