class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        last_ones = 0
        current_ones = 0
        ans = 0
        already_zero = 0
        has_zero = 1
        for num in nums:
            if num == 1:
                # 0 1
                if already_zero == 1:
                    ans = max(ans, last_ones + current_ones)
                    last_ones = current_ones
                    current_ones = 0
                    already_zero = 0
                current_ones += 1
            if num == 0:
                has_zero = 0
                if already_zero:
                    last_ones = 0
                    current_ones = 0
                else:
                    # 1 0
                    ans = max(ans, current_ones + last_ones)
                    already_zero = 1

        ans = max(ans, last_ones + current_ones)

        return ans - has_zero
