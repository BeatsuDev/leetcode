from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isnumeric():
                stack.append(int(token))
                continue

            b, a = stack.pop(), stack.pop()

            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "/":
                stack.append(int(a/b))
            elif token == "*":
                stack.append(a*b)

        return stack[0]
