#!/usr/bin/python3


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.cap = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p
        node.next = None
        node.prev = None

    def insert(self, node):
        n = self.head.next
        self.head.next = node
        node.next = n
        n.pre = node
        node.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.cap:
                delete_node = self.tail.prev
                del self.cache[delete_node.key]
                self.remove(delete_node)
            node = Node(key, value)
            self.insert(key, value)
            self.insert(node)
            self.cache[key] = node