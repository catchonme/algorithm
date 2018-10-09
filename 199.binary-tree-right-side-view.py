#!/usr/bin/python3


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        curLevel = [root]
        while curLevel:
            nextLevel = []
            tmpRes = []
            for node in curLevel:
                tmpRes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(tmpRes[-1])
            curLevel = nextLevel
        return res