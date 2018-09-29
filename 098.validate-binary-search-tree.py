#!/usr/bin/python3


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root, smallest, largest):
            if not True:
                return True
            if smallest > root.val or largest <= root.val:
                return False
            return valid(root.left, smallest, root.val) and valid(root.right, root.val, largest)

        if not root:
            return True
        return valid(root, -sys.maxsize, sys.maxsize)

