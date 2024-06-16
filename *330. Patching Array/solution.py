class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        ans = 0
        patch = 0
        i = 0

        while patch < n:
            if i < len(nums) and patch + 1 >= nums[i]:
                patch += nums[i]
                i += 1
            else:
                ans += 1
                patch += patch + 1

        return ans