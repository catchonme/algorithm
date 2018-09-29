#!/usr/bin/python3


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(n, k, 1, [], ans)
        return ans

    def dfs(self, n, k, start, lst, ans):
        if k == 0:
            ans.append(lst)
            return
        for i in range(start, n+1):
            self.dfs(n, k-1, i+1, lst+[i], ans)


sol = Solution()
res = sol.combine(4, 2)
print(res)