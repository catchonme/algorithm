#!/usr/bin/python3


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        return (C - A) * (D - B) + (H - F) * (G - E) - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)


sol = Solution()
res = sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
print(res)