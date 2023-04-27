class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [0 for i in range(len(nums))]
        dp[0] = 1 if nums[0] else 0
        for i in range(len(nums)):
            if dp[-1]:
                return True
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < len(nums):
                        dp[i + j] = 1
        return dp[-1]
