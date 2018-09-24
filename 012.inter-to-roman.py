#!/usr/bin/python3


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lookup = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        romanStr = ''

        for symbol, val in sorted(lookup.items(), key=lambda t: t[1], reverse=True):
            while num >= val:
                romanStr += symbol
                num -= val
        return romanStr


sol = Solution()
res = sol.intToRoman(5)
print(res)