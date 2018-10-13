#!/usr/bin/python3


class Solution(object):
    cache = {}

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        from math import sqrt
        if n < 4:
            return []
        if n in self.cache:
            return self.cache[n]
        else:
            res = []
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0 and i <= n / i:
                    res.append([i] + [int(n / i)])
                    for j in self.getFactors(n / i):
                        if j and i <= j[0]:
                            res.append([i] + j)
            self.cache[n] = res
        return res


sol = Solution()
result = sol.getFactors(32)
print(result)