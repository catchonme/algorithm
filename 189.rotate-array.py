#!/usr/bin/python3

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            tmp = nums[-k:]
            for j in range(len(nums)-1, k-1, -1):
                nums[j] = nums[j-k]
            nums[:k] = tmp


arr = [1, 2, 3, 4, 5, 6, 7]
sol = Solution()
sol.rotate(arr, 3)
print(arr)


class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


arr1 = [1, 2, 3, 4, 5, 6, 7]
sol1 = Solution1()
sol1.rotate(arr1, 3)
print(arr1)