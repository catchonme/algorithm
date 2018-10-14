#!/usr/bin/python3


class Solution(object):
    def canAttendMeetings(self, intervals):
        if not intervals or len(intervals) < 2:
            return True
        intervals = sorted(intervals, key=lambda x:(x[0], x[1]))
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


sol = Solution()
res = sol.canAttendMeetings([[7, 10], [2, 4]])
print(res)