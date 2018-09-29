#!/usr/bin/python3


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead
        """
        red, white, blue = 0, 0, 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
        for i in range(red):
            nums[i] = 0
        for i in range(red, red+white):
            nums[i] = 1
        for i in range(red+white, len(nums)):
            nums[i] = 2


numsInput = [2, 0, 2, 1, 1, 0]
sol = Solution()
sol.sortColors(numsInput)
print(numsInput)