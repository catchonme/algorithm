#!/usr/bin/python3


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for i in sorted(intervals, key=lambda x: x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res


sol = Solution()
output = sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print(output)