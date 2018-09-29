#!/usr/bin/python3


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''

        factorial = [1] * (n + 1)
        # factorial[] = [1, 1, 2, 6, 24, ... n!]
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        # create a list of numbers to get indices
        nums = [i for i in range(1, n + 1)]
        # because we start from index 0
        k -= 1

        for i in range(1, n + 1):
            # this is the idx of first num each time we will get
            idx = k / factorial[n - i]
            res += str(nums[idx])
            # delete this num, since we have got it
            nums.pop(idx)
            # update k
            k -= idx * factorial[n - i]
        return res


sol = Solution()
output = sol.getPermutation(3, 3)
print(output)