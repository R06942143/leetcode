class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if dp[i] or i == 0:
                for j in range(1, nums[i] + 1):
                    if i + j >= len(nums):
                        break
                    if dp[i + j]:
                        dp[i + j] = min(dp[i] + 1, dp[i + j])
                    else:
                        dp[i + j] = dp[i] + 1
        return dp[-1]
