#!/usr/bin/python3


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums)-1


sol = Solution()
res = sol.findPeakElement([1, 2, 3, 1])
print(res)