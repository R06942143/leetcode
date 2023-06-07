from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(int)
        for word in s:
            sMap[word] += 1
        for word in t:
            sMap[word] -= 1
        for _, value in sMap.items():
            if value != 0:
                return False
        return True
