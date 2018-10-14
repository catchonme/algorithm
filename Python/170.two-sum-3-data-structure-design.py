#!/usr/bin/python3


class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.lookup = {}
        self.lst = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.lst.append(number)
        self.lookup[number] = self.lookup.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value
        :type value: int
        :rtype: bool
        """
        for num in self.lst:
            if value - num in self.lookup:
                if value == 2 * num and self.lookup[num] >= 2:
                    return True
                elif value != 2 * num:
                    return True
        return False


obj = TwoSum()
obj.add(1)
obj.add(2)
res = obj.find(3)
res1 = obj.find(4)
print(res)
print(res1)