#!/usr/bin/python3

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        idx, step = 0, 1

        for x in s:
            res[idx] += x
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(res)


sol = Solution()
res = sol.convert("PAYPALISHIRING", 4)
print(res)