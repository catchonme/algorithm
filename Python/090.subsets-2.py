#!/usr/bin/python3


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]

        for i in range(len(nums)):
            res.extend([tmp+[nums[i]] for tmp in res if tmp.count(nums[i]) == i - nums.index(nums[i])])
        return res


sol = Solution()
output = sol.subsetsWithDup([1, 2, 2])
print(output)
