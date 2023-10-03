class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        num_map = {}
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] += 1
        ans = 0
        for _, value in num_map.items():
            ans += value*(value - 1)/2
        return int(ans)