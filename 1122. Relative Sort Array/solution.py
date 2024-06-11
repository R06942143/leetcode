from collections import defaultdict


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        num_map = defaultdict(int)

        for i in range(len(arr1)):
            num_map[arr1[i]] += 1

        ans = []
        for key in arr2:
            ans = ans + [key] * num_map[key]
            del num_map[key]
        
        keys = list(num_map.keys())
        for key in sorted(keys):
            ans = ans + [key] * num_map[key]
        
        return ans
        