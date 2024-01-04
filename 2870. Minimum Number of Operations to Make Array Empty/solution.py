from collections import defaultdict
import math


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        nums_map = defaultdict(int)
        for num in nums:
            nums_map[num] += 1
        
        ans = 0

        for _, value in nums_map.items():
            if value == 1:
                return -1
            ans += math.ceil(value / 3)
        
        return ans
