class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        ops = 0
        prev = float("INF")
        for num in reversed(nums):
            if num > prev:
                times = (num + prev - 1) // prev
                prev = num // times
                ops += times - 1
            else:
                prev = num
        return ops