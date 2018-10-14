#!/usr/bin/python3


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        idx = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:  # find first number which is smaller than it's after number
                idx = i
                break
        if idx != 0:  # if the number exist,which means that the nums not like{5,4,3,2,1}
            for i in range(len(nums) - 1, idx - 1, -1):
                if nums[i] > nums[idx - 1]:
                    nums[i], nums[idx - 1] = nums[idx - 1], nums[i]
                    break

        nums[idx:] = nums[idx:][::-1]
        return nums


sol = Solution()
res = sol.nextPermutation([1, 2, 3])
print(res)
