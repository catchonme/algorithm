#!/usr/bin/python3


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.calSum(root, 0)

    def calSum(self, root, curSum):
        if root is None:
            return 0
        else:
            curSum = curSum * 10 + root.val
            if root.left is None and root.right is None:
                return curSum
            else:
                return self.calSum(root.left, curSum) + self.calSum(root.right, curSum)
