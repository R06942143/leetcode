class Solution:
    def firstUniqChar(self, s: str) -> int:
        position_map = {}
        
        for i in range(len(s)):
            if s[i] in position_map:
                position_map[s[i]] = -1
            else:
                position_map[s[i]] = i
        
        for char in s:
            if position_map[char] != -1:
                return position_map[char]
        return -1