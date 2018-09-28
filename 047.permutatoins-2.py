#!/usr/bin/python3


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            prefix = nums[i]
            rest = nums[:i] + nums[i+1:]
            for j in self.permuteUnique(rest):
                if [prefix]+j not in res:
                    res.append([prefix]+j)
        return res


sol = Solution()
res = sol.permuteUnique([1, 1, 2])
print(res)