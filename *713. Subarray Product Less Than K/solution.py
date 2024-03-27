class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        total_count = 0
        product = 1

        left = 0
        for right, num in enumerate(nums):
            product *= num  # Expand the window by including the element at the right pointer

            while product >= k:
                product //= nums[left]  # Remove the element at the left pointer from the product
                left += 1

            total_count += right - left + 1  # right - left + 1 represents the current window size

        return total_count