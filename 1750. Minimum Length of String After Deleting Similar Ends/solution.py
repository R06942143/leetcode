class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        while left < right and s[left] == s[right]:
            while left < len(s) - 1 and s[left] == s[left + 1]:
                left += 1
            
            while right > 0 and s[right] == s[right - 1]:
                right -= 1
            
            left += 1
            right -= 1

        if left > right:
            return 0
        else:
            return right - left +1
