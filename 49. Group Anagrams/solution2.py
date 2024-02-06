from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans_map = defaultdict(list)
        for string in strs:
            order_string = "".join(sorted(string))
            ans_map[order_string].append(string)
        
        return ans_map.values()