from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_map = defaultdict(int)
        for character in s:
            character_map[character] += 1
        
        for character in t:
            character_map[character] -= 1

        for _, value in character_map.items():
            if value != 0:
                return False
        
        return True