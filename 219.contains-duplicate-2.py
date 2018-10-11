#!/usr/bin/python3


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        lookup = {}
        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = i
            else:
                if i - lookup[nums[i]] <= k:
                    return True
                else:
                    lookup[nums[i]] = i
        return False

