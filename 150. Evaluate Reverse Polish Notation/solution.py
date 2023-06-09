class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token.isnumeric() or (token[0] == "-" and token[1:].isnumeric()):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "/":
                    stack.append(int(first / second))
        return stack[-1]
