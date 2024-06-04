from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        has_single_one = 0
        s_map = defaultdict(int)
        ans = 0
        for char in s:
            s_map[char] += 1

        for value in s_map.values():
            if value % 2 ==0:
                ans += value
            else:
                has_single_one = 1
                ans += (value - 1)
        
        return ans + has_single_one