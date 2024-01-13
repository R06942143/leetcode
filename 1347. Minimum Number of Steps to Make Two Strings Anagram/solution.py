from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for c in s:
            s_map[c] += 1
        
        for c in t:
            t_map[c] += 1
        
        for key, value in s_map.items():
            t_map[key] -= value
        ans = 0
        for _, value in t_map.items():
            if value < 0:
                ans -= value
            else:
                ans += value
        
        return ans //2