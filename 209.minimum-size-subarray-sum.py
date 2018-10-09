#!/usr/bin/python3

import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, end, sums, res = 0, 0, 0, sys.maxsize
        while end < len(nums):
            sums += nums[end]
            end += 1
            while sums >= s:
                sums -= nums[start]
                start += 1
                res = min(res, end-start+1)
        return res if res != sys.maxsize else 0


sol = Solution()
result = sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(result)