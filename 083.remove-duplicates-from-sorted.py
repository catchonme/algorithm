#!/usr/bin/python3


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next  # skip duplicated node
            head = head.next
        return dummy
