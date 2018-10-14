#!/usr/bin/python3


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.auxPathSum(root, sum, [], res)
        return res
    def auxPathSum(self, root, sum, cur_list, cur_lists):
        if not root:
            return
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            cur_lists.append(cur_list + [root.val])
            return
        if root.left:
            self.auxPathSum(root.left, sum, cur_list + [root.val], cur_lists)
        if root.right:
            self.auxPathSum(root.right, sum, cur_list + [root.val], cur_lists)