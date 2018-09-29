#!/usr/bin/python3


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype:
        """
        def buildTree(inorder, postorder, li, ri, lp, rp):
            if lp > rp or li > ri:
                return None

            root = TreeNode(postorder[rp])
            k = inorder.index(postorder[rp])

            left = buildTree(inorder, postorder, li, k-1, lp, lp + k - li -1)
            right = buildTree(inorder, postorder, k+1, ri, lp+k-li, rp-1)

            root.left = left
            root.right = right

            return root
        return buildTree(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)