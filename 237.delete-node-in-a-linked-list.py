#!/usr/bin/python3


class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.nextga