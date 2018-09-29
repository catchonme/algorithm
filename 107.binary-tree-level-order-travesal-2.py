#!/usr/bin/python3

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, level, res):
            if not node:
                return
            if len(res) < level:
                res.append([])
            res[level-1].append(node.val)
            dfs(node.left, level+1, res)
            dfs(node.right, level+1, res)

        res = []
        dfs(root, 1, res)
        return res[::1]