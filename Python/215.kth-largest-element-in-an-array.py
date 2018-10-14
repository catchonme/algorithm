#!/usr/bin/python3


class Solution(object):
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        smaller = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        greater = [num for num in nums if num > pivot]

        if len(greater) >= k:
            return self.findKthLargest(greater, k)
        elif len(equal) >= (k - len(greater)):
            return equal[0]
        else:
            return self.findKthLargest(smaller, k - len(greater) - len(equal))


sol = Solution()
res = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(res)