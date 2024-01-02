from collections import defaultdict


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        nums_map = defaultdict(int)
        for num in nums:
            nums_map[num] += 1
        
        ans = []

        for key, value in nums_map.items():
            while len(ans) < value:
                ans.append([])
            for i in range(value):
                ans[i].append(key)
        
        return ans
