from collections import defaultdict


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_map = defaultdict(int)
        for char in chars:
            char_map[char] += 1
        ans = 0
        for word in words:
            flag = True
            tmp_map = defaultdict(int)
            for w in word:
                tmp_map[w] += 1
            
            for key, value in tmp_map.items():
                if tmp_map[key] > char_map[key]:
                    flag = False
            if flag:
                ans += len(word)
        
        return ans
