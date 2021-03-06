#!/usr/bin/python3


class Solution(object):
    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list(set((R, 0, None) for L, R, H in buildings)))
        res, hp = [[0, 0]], [(0, float('inf'))]
        for x, negH, R in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if negH: heapq.heappush(hp, (nepgH, R))
            if res[-1][1] + hp[0][0]:
                res += [x, -hp[0][0]]
        return res[1:]


