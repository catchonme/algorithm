#!/usr/bin/python3


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            for j in range(i+1, n):
                l, r = j+1, n-1
                while l < r:
                    temp = nums[i] + nums[j] + nums[l] + nums[r]
                    if temp == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif temp > target:
                        r -= 1
                    else:
                        l += 1
        return res


sol = Solution()
res = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
print(res)