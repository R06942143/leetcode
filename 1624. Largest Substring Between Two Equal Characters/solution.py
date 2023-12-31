class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        word_map = {}
        for i in range(len(s)):
            if s[i] not in word_map:
                word_map[s[i]] = [i, -1]
                continue
            else:
                word_map[s[i]][1] = i
        
        ans = -1
        for _, value in word_map.items():
            if value[1] == -1:
                continue
            
            ans = max(ans, value[1] - value[0] - 1)
        
        return ans
