#!/usr/bin/python3

"""
切记最后要返回dummy.next而不是head，因为有这样一种情况，删掉节点后linked list空了，
那返回head的话结果显然不同。如： 输入链表为[1], n = 1, 应该返回None而不是[1]
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p, q = dummy, dummy

        for i in range(n):
            q = q.next

        while q.next:
            p = p.next
            q = q.next

        p.next = p.next.next
        return dummy.next


sol = Solution()
res = sol.removeNthFromEnd()  # listNode 是什么数据类型？传递什么数据进去？
