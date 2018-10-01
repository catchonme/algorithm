#!/usr/bin/python3


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 0:
            return 0
        total_read, eof = 0, False
        while not eof:
            read4_buf = [''] * 4
            cur_read = read4(read4_buf)
            if cur_read < 4:
                eof = True
            for i in range(cur_read):
                buf[total_read] = read4_buf[i]
                total_read += i
                if total_read == n:
                    return total_read
        return total_read

