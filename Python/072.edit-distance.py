#!/usr/bin/python3


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        # 这里第一行第一列初始值一定要为i+j，因为当另一个单词为空的时候很明显至少需要i或者j次edit
        dp = [[i+j for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2)+1):
                tmp_dist = 0 if word1[i-1] == word2[j-1] else 1
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1], dp[i-1][j-1]+tmp_dist)
        return dp[-1][-1]


sol = Solution()
res = sol.minDistance('word1', 'ord')
print(res)

