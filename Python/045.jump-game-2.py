#!/usr/bin/python3


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Note You can assume that you can always reach the last index.
        cur_end, cur_farthest, step, n = 0, 0, 0, len(nums)
        for i in range(n-1):
            cur_farthest = max(cur_farthest, i + nums[i])
            if cur_farthest >= n - 1:
                step += 1
                break
            if i == cur_end:
                cur_end = cur_farthest
                step += 1
        return step


sol = Solution()
res = sol.jump([2, 3, 1, 1, 4])
print(res)