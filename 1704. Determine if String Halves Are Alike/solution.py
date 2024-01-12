class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def mapping(char: str) -> int:
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                return 1
            return 0
        a = 0
        b = 0

        for i in range(len(s)//2):
            if mapping(s[i]) == 1:
                a += 1
            if mapping(s[len(s)//2 + i]) == 1:
                b += 1


        return a == b