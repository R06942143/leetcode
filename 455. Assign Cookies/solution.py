from collections import deque


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        s_deque = deque(s)
        ans = 0
        i = 0
        while len(s_deque) > 0 and i < len(g):
            current = s_deque.popleft()
            if current >= g[i]:
                ans += 1
                i += 1
        
        return ans
