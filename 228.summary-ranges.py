#!/usr/bin/python3


class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        for i in nums:
            if not ranges or i > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = i,  # 这两个逗号有什么用？去掉了就出错了
        return ['->'.join(map(str, r)) for r in ranges]


sol = Solution()
res = sol.summaryRanges([0, 1, 2, 4, 5, 7])
print(res)