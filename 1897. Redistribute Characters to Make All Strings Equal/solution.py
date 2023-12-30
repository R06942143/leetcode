from collections import defaultdict


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        word_map = defaultdict(int)
        for word in words:
            for character in word:
                word_map[character] += 1

        n = len(words)
        for _, value in word_map.items():
            if value % n != 0:
                return False
        

        return True
