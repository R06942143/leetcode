class Solution:
    def numSteps(self, s: str) -> int:
        s_int = 0
        for i in s:
            s_int *= 2
            s_int += int(i)
        
        step = 0
        
        while s_int != 1:
            if s_int % 2 == 0:
                s_int //= 2
                step += 1
            else:
                s_int += 1
                step += 1

        return step