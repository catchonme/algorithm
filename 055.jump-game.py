#!/usr/bin/python3


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        if len(nums) == 1:
            return True
        n = len(nums)
        idx, reach = 0, 0
        while idx < n-1 and idx <= reach:  # idx <= reach 是为了处理nums[idx] == 0 的情况，若idx>reach 说明已经失败了
            reach = max(reach, idx+nums[idx])
            idx += 1
        return reach >= n-1


sol = Solution()
res = sol.canJump([3, 2, 1, 0, 4])
print(res)