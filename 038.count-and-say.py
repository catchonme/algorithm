#!/usr/bin/python3

"""
i代表字符下标，从0开始取值，也就是从第一个字符开始，因为要让i取到最后一个字符，并且后面还要进行i+1的操作，所以将原字符串随意加上一个‘*’字符防止溢出
count代表此时已经连续相同的字符个数
res代表最终输出的字符串
只要i下标对应的字符等于下一个字符，则sum和i都加1，无限循环
如果i下标对应的字符不等于下一个字符了，则res应该加上str(sum)和i下标对应的那个字符，并且i加1，sum复原回0
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1) + '*'
        res, count = '', 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                count += 1
            else:
                res += str(count) + str(s[i])
                count = 1
        return res


sol = Solution()
res = sol.countAndSay(4)
print(res)

