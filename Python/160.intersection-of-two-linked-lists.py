#!/usr/bin/python3


class Solution(object):
    def getIntersection(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA