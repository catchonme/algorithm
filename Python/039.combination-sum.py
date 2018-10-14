#!/usr/bin/python3


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, combo, index):
            if remain == 0:
                res.append(combo)
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break
                dfs(remain - candidates[i], combo + [candidates[i]], i)
        candidates = list(set(candidates))
        candidates.sort()
        res = []
        dfs(target, [], 0)
        return res


sol = Solution()
res = sol.combinationSum([2, 3, 6, 7], 7)
print(res)