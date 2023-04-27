import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.isqrt(n)


# When we see the number, it will be 1 if its factors are odd, and 0 if its factors are even.
# The only numbers that have odd factors are the perfect squares.
