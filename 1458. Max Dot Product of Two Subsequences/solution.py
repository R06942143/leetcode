from functools import cache


class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        @cache
        def dp(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0
            now = nums1[i] * nums2[j] + dp(i + 1, j + 1)

            return max(now, dp(i, j + 1), dp(i + 1, j))

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        return dp(0,0)