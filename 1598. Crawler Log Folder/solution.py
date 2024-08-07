class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for log in logs:
            if log != './':
                if log == '../':
                    if stack:
                        stack.pop()
                else:
                    stack.append(log)
        return len(stack)
        