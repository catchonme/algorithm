#!/usr/bin/python3


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last+num, now)
        return now


sol = Solution()
res = sol.rob([1, 2, 3, 4, 5])
print(res)