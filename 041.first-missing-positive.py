#!/usr/bin/python3


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        old_missing, missing = 0, 1
        while old_missing != missing:
            old_missing = missing
            for i in range(len(nums)):
                if nums[i] == missing:
                    missing += 1
        return missing


sol = Solution()
res = sol.firstMissingPositive([7, 8, 9, 11, 12])
print(res)