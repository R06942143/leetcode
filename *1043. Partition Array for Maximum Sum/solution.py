class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)


        for i in range(n-1,-1,-1):
            curr_max = 0

            for j in range(i, min(n,i+k)):
                if curr_max<arr[j]:
                    curr_max = arr[j]
                dp[i] = max(dp[i], dp[j+1]+curr_max*(j-i+1))

        return dp[0]
