#!/usr/bin/python3


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :type: TreeNode
        """
        if not nums:
            return None
        if nums:
            mid = len(nums) / 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root