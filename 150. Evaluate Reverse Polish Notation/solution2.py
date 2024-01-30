class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(token))
        return stack[0]