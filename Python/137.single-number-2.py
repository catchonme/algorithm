#!/usr/bin/python3


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((3 * sum(set(nums)) - sum(nums)) / 2)


sol = Solution()
result = sol.singleNumber([0, 1, 0, 1, 0, 1, 99])
print(result)
