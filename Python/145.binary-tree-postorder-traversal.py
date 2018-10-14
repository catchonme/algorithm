#!/usr/bin/python3


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        if left:
            res.extend(left)
        if right:
            res.extend(right)

        res.append(root.val)
        return res