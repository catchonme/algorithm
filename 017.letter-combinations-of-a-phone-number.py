#!/usr/bin/python3

"""
hash table一个，用来对应digit -> letter
s用来记录结果，每次从digits里面去一个，然后寻找其可能的char，加到s中，digits长度减小
digits长度为0时候，把它加入结果
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []

        def helper(s, digits):
            if len(digits) == 0:
                res.append(s)
            else:
                cur_digit = digits[0]
                for char in lookup[cur_digit]:
                    helper(s+char, digits[1:])

        if not digits or len(digits) == 0:
            return res
        helper('', digits)
        return res


sol = Solution()
res = sol.letterCombinations("23")
print(res)