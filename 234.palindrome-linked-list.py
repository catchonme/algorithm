#!/usr/bin/python3


class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True