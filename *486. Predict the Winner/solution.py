class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])

        return dp[0] >= 0
