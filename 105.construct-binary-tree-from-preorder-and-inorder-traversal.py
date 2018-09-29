#!/usr/bin/python3

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        k = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:k+1], inorder[0:k])
        root.right = self.buildTree(preorder[k+1:], inorder[k+1:])
        return root