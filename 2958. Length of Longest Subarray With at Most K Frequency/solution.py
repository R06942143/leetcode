from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        num_map = defaultdict(int)

        ans = 0

        left = 0
        right = 0
        while left < len(nums) and right < len(nums):
            num_map[nums[right]] += 1

            while num_map[nums[right]] > k:
                num_map[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
        
        return ans 