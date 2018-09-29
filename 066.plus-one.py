#!/usr/bin/python3


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []:
            return [1]
        if digits[-1] < 9:
            return digits[:-1] + [digits[-1] + 1]
        else:
            return self.plusOne(digits[:-1]) + [0]


sol = Solution()
res = sol.plusOne([1, 2, 3])
print(res)