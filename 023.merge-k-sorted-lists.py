#!/usr/bin/python3


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype : ListNode
        """
        from heapq import heappush, heappop
        nodes_pool = []
        dummy = cur = ListNode(-1)
        for head in lists:
            if head:
                heappush(nodes_pool, [head.val, head])
        while nodes_pool:
            smallest_node = heappop(nodes_pool)[1]
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heappush(nodes_pool, [smallest_node.next.val, smallest_node.next])
        return dummy.next

