from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_map = defaultdict(int)
        word2_map = defaultdict(int)

        for c in word1:
            word1_map[c] += 1
        
        for c in word2:
            word2_map[c] += 1
        
        return sorted(word1_map.values()) == sorted(word2_map.values()) and sorted(word1_map.keys()) == sorted(word2_map.keys())