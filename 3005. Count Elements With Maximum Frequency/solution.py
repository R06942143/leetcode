from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
        
        max_f = max(num_map.values())
        ans = 0
        for value in num_map.values():
            if value == max_f:
                ans += max_f
        
        return ans