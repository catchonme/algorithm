#!/usr/bin/python3
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]:
        """
        look_up = {}
        for i, num in enumerate(nums):
            if target - num in look_up:
                return [look_up[target-num], i]
            look_up[num] = i
        return []


sol = Solution()
res = sol.twoSum([2, 7, 11, 15], 18)
print(res)
