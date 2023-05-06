class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        mod = 10**9 + 7
        ans = 0
        r, l = len(nums) - 1, 0
        nums.sort()
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += 2 ** (r - l)
                l += 1
        return ans % mod
