#!/usr/bin/python3


class Solution(object):
    def __init__(self):
        self.lst = []

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        self.lst.remove(self.lst[-1])

    def top(self):
        return self.lst[-1]

    def empty(self):
        return self.lst == []