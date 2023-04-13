class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped.reverse()
        tmp = popped.pop()
        stack = []
        for number in pushed:
            while(stack and stack[-1] == tmp):
                stack.pop()
                if popped:
                    tmp = popped.pop()
                else:
                    return stack == []
            if number == tmp:
                if popped:
                    tmp = popped.pop()
                else:
                    return stack == []
            else:
                stack.append(number)
        return stack == popped + [tmp]