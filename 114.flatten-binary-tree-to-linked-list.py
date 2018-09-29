#!/usr/bin/python3


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead
        """
        def preorder(root):
            res = []
            if not root:
                return res
            res.append(root)
            if root.left:
                res.extend(preorder(root.left))
            if root.right:
                res.extend(preorder(root.right))
            return res
        if not root:
            return
        node_order = preorder(root)
        for i in range(len(node_order) - 1):
            node_order[i].left = None
            node_order[i].right = node_order[i+1]
        node_order[-1].left = None
        node_order[-1].right = None