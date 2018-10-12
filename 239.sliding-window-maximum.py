#!/usr/bin/python3


from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or len(nums) == 0:
            return []
        if k == 0:
            return nums
        deq, res = deque(), []

        for i in range(k):
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        for i in range(k, len(nums)):
            res.append(nums[deq[0]])
            if deq[0] < i - k + 1:
                deq.popleft()

            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        res.append(nums[deq[0]])
        return res


sol = Solution()
result = sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)