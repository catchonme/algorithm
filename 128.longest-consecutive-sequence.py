#!/usr/bin/python3


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                y = num + 1
                while y in nums:
                    y += 1
                res = max(res, y-num)
        return res


sol = Solution()
result = sol.longestConsecutive([100, 4, 200, 1, 3, 2])
print(result)