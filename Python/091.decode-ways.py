#!/usr/bin/python3


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24', '25', '26']
        values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'R', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
        numbersToLetters = dict(zip(keys, values))

        ways = {}
        n = len(s)
        for i in range(n):
            ways[i] = 0
        if n == 0:
            return 0
        elif n == 1:
            ways[0] == int(s in numbersToLetters)
        elif n == 2:
            if (s[0] in numbersToLetters) and (s[1] in numbersToLetters):
                ways[1] += 1
            if s in numbersToLetters:
                ways[1] += 1
        else:
            ways[0] = int(s[0] in numbersToLetters)
            if (s[0] in numbersToLetters) and (s[1] in numbersToLetters):
                ways[1] += 1
            if s[:2] in numbersToLetters:
                ways[1] += 1
            for i in range(2, n):
                if s[i] in numbersToLetters:
                    ways[i] += ways[i-1]
                if s[i-1:i+1] in numbersToLetters:
                    ways[i] += ways[i-2]

        return ways[n-1]


sol = Solution()
res = sol.numDecodings("226")
print(res)