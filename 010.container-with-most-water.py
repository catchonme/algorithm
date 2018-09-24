#!/usr/bin/python3

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n-1
        most_water = 0
        while left <= right:
            water = (right - left) * min(height[left], height[right])
            most_water = max(water, most_water)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return most_water


sol = Solution()
res = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(res)