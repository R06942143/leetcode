class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        r = 0
        now = 0
        ans = float("INF")
        while r < len(nums):
            now += nums[r]
            r += 1
            while now >= target:
                ans = min(ans, r - l)
                now -= nums[l]
                l += 1
        if ans == float("INF"):
            return 0
        return ans
