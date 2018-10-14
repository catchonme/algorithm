#!/usr/bin/python3


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxdp = [nums[0] for i in range(n)]
        mindp = [nums[0] for i in range(n)]

        for i in range(1, n):
            maxdp[i] = max(mindp[i-1]*nums[i], maxdp[i-1]*nums[i], nums[i])
            mindp[i] = min(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])

        return max(maxdp)


sol = Solution()
result = sol.maxProduct([2, 3, -2, 4])
print(result)