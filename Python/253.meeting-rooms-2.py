#!/usr/bin/python3


from heapq import heappush, heappop
class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        end = []
        for it in intervals:
            if end and end[0] <= it[0]:
                heappop(end)
            heappush(end, it[1])
        return len(end)


sol = Solution()
res = sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
print(res)