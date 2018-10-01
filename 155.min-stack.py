#!/usr/bin/python3

from collections import deque
class MinStack(object):
    def __init__(self):
        self.lst = deque()
        self.aux = deque()

    def push(self, x):
        self.lst.append(x)
        if not self.aux or self.aux[-1] > x:
            self.aux.append(x)
        else:
            self.aux.append(self.aux[-1])


    def pop(self):
        self.lst.pop()
        self.aux.pop()

    def top(self):
        return self.lst[-1]

    def getMin(self):
        return self.aux[-1]