#!/usr/bin/python3

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root:TreeNode
        :rtype: int
        """
        self.global_max = root.val if root else 0
        self.findmax(root)
        return self.global_max

    def findmax(self, node):
        if not node:
            return 0

        left = self.findmax(node.left)
        left = left if left > 0 else 0

        right = self.findmax(node.right)
        right = right if right > 0 else 0
        self.global_max = max(left + right + node.val, self.global_max)
        return max(left, right) + node.val

