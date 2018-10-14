#!/usr/bin/python3


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :type: int
        """
        isPrime = [1 for i in range(n)]

        i = 2
        while i * i < n:
            if isPrime[i]:
                j = i * i
                while j < n:
                    isPrime[j] = 0
                    j += i
            i += 1
        return sum(isPrime[2:])


sol = Solution()
res = sol.countPrimes(10)
print(res)