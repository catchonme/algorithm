#!/usr/bin/python3


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        area = 0
        for row in matrix:
            for col_num, item in enumerate(row):
                # for each cell with value = 1, we look upward (north), the number of continuous '1' is the height of cell
                heights[col_num] = heights[col_num] + 1 if item == '1' else 0
            area = max(area, self.largestRectangleArea(heights))
        return area

    def largestRectangleArea(self, heights):
        left_stack, right_stack = [], []
        left_indexes, right_indexes = [-1] * len(heights), [len(heights)] * len(heights)

        for i in range(len(heights)):
            while left_stack and heights[i] < heights[left_stack[-1]]:
                right_indexes[left_stack.pop()] = i
            left_stack.append(i)

        for i in range(len(heights)-1, -1, -1):
            while right_stack and heights[i] < heights[right_stack[-1]]:
                left_indexes[right_stack.pop()] = i
            right_stack.append(i)

        res = 0
        for i in range(len(heights)):
            area = heights[i] * (right_indexes[i] - left_indexes[i] - 1)
            res = max(res, area)

        return res


inputMatrix = [
  ["1", "0", "1", "0", "0"],
  ["1", "0", "1", "1", "1"],
  ["1", "1", "1", "1", "1"],
  ["1", "0", "0", "1", "0"]
]
sol = Solution()
output = sol.maximalRectangle(inputMatrix)
print(output)
