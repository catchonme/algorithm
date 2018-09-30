#!/usr/bin/python3


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in nums[1:]:
            res ^= i
        return res


sol = Solution()
result = sol.singleNumber([4,1,2,1,2])
print(result)