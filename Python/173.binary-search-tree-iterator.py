#!/usr/bin/python3


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.pushAllLeft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            cur = self.stack.pop()
            if cur.right:
                self.pushAllLeft(cur.right)
            return cur.val

    def pushAllLeft(self, node):
        """
        :type node: TreeNode
        """
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left
