class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        ans = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += pow(2, (r - l), 1000000007)
                l += 1
            else:
                r -= 1
        return ans % 1000000007
