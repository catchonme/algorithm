#!/usr/bin/python3


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy.next
        nodeNumber = {}
        while cur:
            if cur.val in nodeNumber:
                nodeNumber[cur.val] += 1
            else:
                nodeNumber[cur.val] = 1

        cur = dummy
        while cur.next:
            if nodeNumber[cur.next.val] > 1:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next