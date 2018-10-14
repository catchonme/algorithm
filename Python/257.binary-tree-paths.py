#!/usr/bin/python3


class Solution(object):
    def binaryTreePaths(self, root):
        def helper(node, cur_path):
            if not node.left and node.right:
                res.append(cur_path + [node.val])
                return
            if node.left:
                helper(node.left, cur_path+[node.val])
            if node.right:
                helper(node.right, cur_path+[node.val])
        res = []
        if not root:
            return res
        helper(root, [])

        return ['->'.join([str(val) for val in path]) for path in res]

