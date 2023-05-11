class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]

        for i in range(1, len(nums2) + 1):
            for j in range(1, len(nums1) + 1):
                if nums2[i - 1] == nums1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
