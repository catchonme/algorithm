#!/usr/bin/python3


class Solution(object):
    def verifyPreorder(self, preorder):
        stack = []
        min_num = -1 << 31
        for x in preorder:
            if x < min_num:
                return False
            while stack and x > stack[-1]:
                min_num = stack.pop()
            stack.append(x)
        return True

