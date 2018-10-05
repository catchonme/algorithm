#!/usr/bin/python3


class Solution(object):
    head, tail, buffer = 0, 0, [''] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.head == self.tail:
                self.head = 0
                self.tail = read4(self.buffer)
                if self.tail == 0:
                    break
            while i < n and self.head < self.tail:
                buf[i] = self.buffer[self.head]
                i += 1
                self.head += 1
        return i