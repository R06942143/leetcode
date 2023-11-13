from collections import deque


class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_map = {}
        for i in range(len(s)):
            if s[i] in set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
                vowel_map[i] = s[i]
        
        vowel_order = deque(sorted(vowel_map.values()))
        t = list(s)
        for key, _ in vowel_map.items():
            t[key] = vowel_order.popleft()
        
        return ''.join(t)