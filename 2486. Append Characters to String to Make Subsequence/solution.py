class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        dp = [0] * len(t)

        i = 0
        for char in s:
            if i < len(t) and char == t[i]:
                dp[i] = 1
                i += 1
        
        return len(t) - sum(dp)