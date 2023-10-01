class Solution:
    def reverseWords(self, s: str) -> str:
        word_stack = []
        ans = ""
        for i in s:
            if i != ' ':
                word_stack.append(i)
            else:
                while word_stack != []:
                    ans += word_stack.pop()
                ans += ' '
        while word_stack != []:
            ans += word_stack.pop()
        return ans