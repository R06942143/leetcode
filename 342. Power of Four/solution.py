class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <1 and n > 0:
            n = 1/n
        while n > 0:
            if n == 1:
                return True
            n_mod = n % 4
            if n_mod != 0:
                return False
            else:
                n = n / 4