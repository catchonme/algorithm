#!/usr/bin/python3

class Solution(object):
    def majorityElement(self, nums):
        cnt1 = 0
        cnt2 = 0
        maj1 = 0
        maj2 = 0
        for num in nums:
            if maj1 == num:
                cnt1 += 1
            elif maj2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                maj1 = num
                cnt1 += 1
            elif cnt2 == 0:
                maj2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = 0
        cnt2 = 0

        n = len(nums)
        res = []
        for num in nums:
            if maj1 == num:
                cnt1 += 1
            elif maj2 == num:
                cnt2 += 1

        if cnt1 > n/3:
            res.append(maj1)
        if cnt2 > n/3:
            res.append(maj2)
        return res


sol = Solution()
result = sol.majorityElement([1, 1, 1, 3, 3, 2, 2, 2])
print(result)