#!/usr/bin/python3


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


sol = Solution()
res = sol.removeElement([1, 2, 3, 3, 4, 4, 5, 3], 3)
print(res)