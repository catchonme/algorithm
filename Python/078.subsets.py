#!/usr/bin/python3


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res.extend([tmp+[num] for tmp in res])
        return res


sol = Solution()
res = sol.subsets([1, 2, 3])
print(res)