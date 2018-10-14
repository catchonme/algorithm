#!/usr/bin/python3


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(nums).lstrip('0') if ''.join(num).lstrip('0') else '0'


sol = Solution()
res = sol.largestNumber([3, 30, 34, 5, 9])
print(res)