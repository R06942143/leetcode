class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.helper(word):
                return word
        return ""

    def helper(self, s: str) -> bool:
        n = len(s)
        for i in range((n+1) // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True
