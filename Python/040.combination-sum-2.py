#!/usr/bin/python3


class Solution(object):
    def combination(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, combo, index):
            if remain == 0 and combo not in res:
                res.append(combo)
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break
                dfs(remain - candidates[i], combo + [candidates[i]], i + 1)

        candidates.sort()
        res = []
        dfs(target, [], 0)
        return res


sol = Solution()
res = sol.combination([10, 1, 2, 7, 6, 1, 5], 8)
print(res)