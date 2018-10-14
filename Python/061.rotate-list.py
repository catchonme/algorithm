#!/usr/bin/python3


class Solution(object):
    def rotateRight(self, head, k):
        if head == None or k == 0:
            return head

        cur = head
        size = 1
        while cur.next:
            size += 1
            cur = cur.next

        tail = cur
        k = k % size
        p = self.findKth(head, k)

        tail.next = head
        head = p.next
        p.next = None
        return head

    def findKth(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = dummy

        for i in range(k):
            q = q.next

        while q.next:
            p = p.next
            q = q.next
        return p


