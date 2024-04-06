class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            elif s[i] == ")":
                if not stack or stack[-1][0] != "(":
                    stack.append((s[i], i))
                else:
                    stack.pop()

        i_set = set()
        for remove in stack:
            i_set.add(remove[1])
        
        ans = ""
        for i in range(len(s)):
            if i not in i_set:
                ans += s[i]
        
        return ans

