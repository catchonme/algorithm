#!/usr/bin/python3


class Solution(object):
    def groupStrings(self, strings):
        table = {}
        for w in strings:
            pattern = ''
            for i in range(1, len(w)):
                if ord(w[i]) - ord(w[i-1]) >= 0:
                    pattern += str(ord(w[i]) - ord(w[i-1]))
                else:
                    pattern += str(ord(w[i]) - ord(w[i-1]) + 26)  # 这里是为了处理 'az' 和 'ba'的情况

            if pattern in table:
                table[pattern].append(w)
            else:
                table[pattern] = [w]

        return [table[pattern] for pattern in table]


sol = Solution()
res = sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
print(res)