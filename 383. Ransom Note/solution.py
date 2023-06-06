from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomMap = defaultdict(int)
        magaMap = defaultdict(int)
        for word in ransomNote:
            ransomMap[word] += 1

        for word in magazine:
            magaMap[word] += 1

        for word, count in ransomMap.items():
            if magaMap[word] < count:
                return False
        return True
