class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        e = lambda x: 1 if x < 2 else 2 if x < 10 else 3 if x < 100 else 4
        @cache
        def f(i, k):
            if i < 0: return 0
            r = f(i-1, k-1) if k else 9e9
            x = 0
            for j in range(i, -1, -1):
                if s[i] == s[j]: x += 1
                elif k == 0: return r
                else: k -= 1
                r = min(r, f(j-1, k) + e(x))
            return r
        return f(len(s)-1, k)