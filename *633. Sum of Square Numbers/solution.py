from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            cur = left * left + right * right
            if cur == c: return True
            if cur < c:
                left += 1
            else:
                right -= 1
        return False