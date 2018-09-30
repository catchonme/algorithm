#!/usr/bin/python3


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        prev = head
        cur = head.next

        while cur:
            p = dummy
            while p.next.val <= cur.val and p != prev:
                p = p.next
            if p != prev:
                prev.next = cur.next
                cur.next = p.next
                p.next = cur
            prev = cur
            cur = cur.next

        return dummy.next