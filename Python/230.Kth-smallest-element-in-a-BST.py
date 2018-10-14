#!/usr/bin/python3


class Solution(object):
    def kthSmallest(self, root, k):
        def count(node):
            if not node:
                return 0
            return count(node.left) + count(node.right) + 1

        if not root:
            return None
        left = count(root.left)
        if left == k - 1:
            return root.val
        elif left > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-left-1)