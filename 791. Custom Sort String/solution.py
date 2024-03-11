from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1
        
        ans_list = []

        for char in order:
            if char in s_map:
                ans_list.append(char*s_map[char])
                del s_map[char]
        
        for key, value in s_map.items():
            ans_list.append(key*value)
        
        return "".join(ans_list)