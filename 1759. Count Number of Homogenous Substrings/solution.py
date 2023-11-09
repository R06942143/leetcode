class Solution:
    def countHomogenous(self, s: str) -> int:
        now_c = s[0]
        now_count = 1
        ans = 0
        modular = 1000000007
        for i in range(1, len(s)):
            if s[i] == now_c:
                now_count += 1
            else:
                ans += (1+now_count) * now_count /2 
                ans = ans % modular
                now_c = s[i]
                now_count = 1
        ans += (1+now_count) * now_count /2 
        ans = ans % modular
        return int(ans)