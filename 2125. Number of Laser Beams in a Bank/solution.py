class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        previous = 0
        now = 0
        for b in bank:
            for security in b:
                if security == '1':
                    now += 1
        
            if now != 0:
                ans += previous * now
                previous = now
                now = 0
        
        return ans
