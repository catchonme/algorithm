#!/usr/bin/python3


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = [nums[0] for i in range(n)]
        for i in range(1, n):
            maxSum[i] = max(maxSum[i-1] + nums[i], nums[i])
        return max(maxSum)


sol = Solution()
res = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)