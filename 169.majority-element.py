#!/usr/bin/python3


class Solution(object):
    def majorityElement(self, nums):
        count, major = 0, 0
        for n in nums:
            if count == 0:
                major = n
            if major == n:
                count += 1
            else:
                count -= 1
        return major