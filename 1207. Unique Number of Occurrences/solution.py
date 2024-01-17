from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr_map = defaultdict(int)
        for i in arr:
            arr_map[i] += 1
        
        return len(arr_map.values()) == len(set(arr_map.values()))