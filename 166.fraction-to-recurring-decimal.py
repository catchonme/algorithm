#!/usr/bin/python3

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:  # zero numerator
            return '0'
        res = ''
        if numerator * denominator < 0:  # determine the sign
            res += '-'
        numerator, denominator = abs(numerator), abs(denominator)  # remove sign of operands
        res += str(numerator / denominator)  # append integer part
        if numerator % denominator == 0:  # in case no fractional part
            return res
        res += '.'
        r = numerator % denominator
        m = {}
        while r:  # simulate the division process
            if r in m:  # meet a known remainder
                res = res[:m[r]] + '(' + res[m[r]:] + ')'  # so we reach the end of the repeating part
                break
            m[r] = len(res)  # if the remainder is first seen, remember next r/denominator index in res
            r *= 10
            res += str(r / denominator)  # append the quotient digit
            r %= denominator

        return res

sol = Solution()
result = sol.fractionToDecimal(1, 2)
print(result)