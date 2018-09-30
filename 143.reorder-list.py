#!/usr/bin/python3


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        n = 0
        dummy1 = head
        while dummy1:
            n += 1
            dummy1 = dummy1.next

        m = n // 2 + 1
        dummy2 = head
        for i in range(m-1):
            dummy2 = dummy2.next
        dummy3 = dummy2.next
        dummy2.next = None

        prev = None
        while dummy3:
            nxt = dummy3.next
            dummy3.next = prev
            prev = dummy3
            dummy3 = nxt

        dummy4 = head
        for i in range(n-m):
            nxt_head = dummy4.next
            nxt_prev = prev.next
            dummy4.next = nxt_head
            prev = nxt_prev
            dummy4 = nxt_head
