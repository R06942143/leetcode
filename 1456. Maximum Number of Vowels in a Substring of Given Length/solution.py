class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = [0] * len(s)
        for i in range(len(s)):
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                vowel[i] = 1

        ans = base = sum(vowel[:k])
        for i in range(k, len(vowel)):
            base = base - vowel[i - k] + vowel[i]
            if base > ans:
                ans = base
        return ans
