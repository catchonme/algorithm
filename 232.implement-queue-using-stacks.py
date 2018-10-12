#!/usr/bin/python3


class Queue(object):
    def __init__(self):
        self.lst = []

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        del self.lst[0]

    def peek(self):
        return self.lst[0]

    def empty(self):
        return self.lst == []