#!/usr/bin/python3


class Solution(object):
    def larestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        area, stack = 0, [-1]

        for idx, height in enumerate(heights):
            while height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = idx - stack[-1] - 1
                area = max(w*h, area)
            stack.append(idx)

        return area


sol = Solution()
res = sol.larestRectangleArea([2, 1, 5, 6, 2, 3])
print(res)