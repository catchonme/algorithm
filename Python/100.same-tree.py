#!/usr/bin/python3

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right)) if p and q else p is q)