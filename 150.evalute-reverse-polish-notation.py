#!/usr/bin/python3


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def cal(op, op1, op2):
            if op == '*':
                return op1 * op2
            elif op == '/':
                return op1 / float(op2)
            elif op == '+':
                return op1 + op2
            else:
                return op1 - op2

        operandStack = []

        for token in tokens:
            if token in '+-*/':
                op2 = operandStack.pop()
                op1 = operandStack.pop()
                res = cal(token, op1, op2)
                operandStack.append(int(res))
            else:
                operandStack.append(int(token))

        return operandStack.pop()


sol = Solution()
res = sol.evalRPN(["2", "1", "+", "3", "*"])
print(res)