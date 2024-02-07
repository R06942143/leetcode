from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        s_map = defaultdict(int)

        for char in s:
            s_map[char] += 1

        order_key = sorted(s_map.keys(), key = lambda char: -s_map[char])
        ans = ""
        for key in order_key:
            ans += key*s_map[key]
        return ans
