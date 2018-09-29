#!/usr/bin/python3


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        if root.left:
            res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        if root.right:
            res.extend(self.inorderTraversal(root.right))
        return res

