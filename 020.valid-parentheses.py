#!/usr/bin/python3


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False

        index = 0
        stack = [i for i in s]
        map1 = {"(": ")", "[": "]", "{": "}"}

        while len(stack) > 0:
            # 判断索引是否超过边界
            if index >= len(stack)-1:
                return False

            b = stack[index]
            e = stack[index+1]

            if b not in map1.keys():
                return False
            elif e in map1.keys():
                index += 1
            elif map1[b] == e:
                stack.pop(index+1)
                stack.pop(index)
                index = 0 if index-1<0 else index-1
            else:
                return False

        return stack == []


sol = Solution()
res = sol.isValid("{[]}")
print(res)
