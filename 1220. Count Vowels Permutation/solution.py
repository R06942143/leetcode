class Solution:
    def countVowelPermutation(self, n: int) -> int:
        modulor = 1000000007
        dp = [1, 1, 1, 1, 1]
        for i in range(n - 1):
            dp_new = [0, 0, 0, 0, 0]
            # a
            dp_new[0] = dp[1]  % modulor

            # e
            dp_new[1] = (dp[0] + dp[2]) % modulor

            # i 
            dp_new[2] = (dp[0] + dp[1] + dp[3] + dp[4]) % modulor

            # o
            dp_new[3] = (dp[2] + dp[4]) % modulor

            # u
            dp_new[4] = dp[0] % modulor
            
            dp = dp_new
        return sum(dp) % modulor