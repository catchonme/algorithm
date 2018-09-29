#!/usr/bin/python3


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        p1 = p2 = dummy
        while p2:
            while p2.next and p2.next.val >= x:
                p2 = p2.next

            if p2.next is None:
                break
            node = p2.next
            p2.next = node.next
            node.next = p1.next
            p1.next = node
            p1 = p1.next

        return dummy.next