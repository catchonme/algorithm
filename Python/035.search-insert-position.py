#!/usr/bin/python3


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while nums[i] < target:
            i += 1
            if i == len(nums):
                return i
        return i


sol = Solution()
res = sol.searchInsert([1, 3, 5, 6], 5)
print(res)