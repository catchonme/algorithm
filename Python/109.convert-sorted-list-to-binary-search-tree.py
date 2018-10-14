#!/usr/bin/python3


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def sortedArrayToBST(nums):
            if not nums:
                return None
            if nums:
                mid = len(nums) / 2
                root = TreeNode(nums[mid])
                root.left = sortedArrayToBST(nums[:mid])
                root.right = sortedArrayToBST(nums[mid+1:])
                return root
        if not head:
            return None
        else:
            lst = []
            while head:
                lst.append(head.val)
                head = head.next
            return sortedArrayToBST(lst)

