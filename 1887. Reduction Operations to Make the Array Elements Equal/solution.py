from collections import defaultdict


class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
        ans = 0
        order = list(num_map.keys())
        order.sort()
        for i in range(1, len(order)):
            ans += num_map[order[i]] * i
        
        return ans