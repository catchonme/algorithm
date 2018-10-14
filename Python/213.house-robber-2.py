#!/usr/bin/python3

class Solution(object):
    def rog(self, nums):
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = nums[j]
                elif j == i + 1:
                    dp[i][j] = max(nums[i], nums[i+1])
                else:
                    dp[i][j] = max(dp[i][j-2] + nums[j], dp[i][j-1])

        val = max(dp[0][n-2], dp[1][n-3] + nums[n-1])
        return val


sol = Solution()
res = sol.rog([1, 2, 3, 1])
print(res)