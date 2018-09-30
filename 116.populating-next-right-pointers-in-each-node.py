#!/usr/bin/python3


class Solution(object):
    def connect(self, root):
        res = []
        self.recurHelper(root, 0, res)
        for level in res:
            for i in range(len(level)-1):
                level[i].next = level[i+1]

    def recurHelper(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root)
        self.recurHelper(root.left, level+1, res)
        self.recurHelper(root.right, level+1, res)