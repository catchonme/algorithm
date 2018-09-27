#!/usr/bin/python3


class Solution(object):
    def removeDumlicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


sol = Solution()
res = sol.removeDumlicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(res)