#!/usr/bin/python3

import math
class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0

        p, q = root, root
        leftHeight = 0
        rightHeight = 0

        while p:
            p = p.left
            leftHeight += 1

        while q:
            q = q.right
            rightHeight += 1

        if leftHeight == rightHeight:
            return (int)(math.pow(2, leftHeight) - 1)
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)