class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        negative = 1
        positive = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                negative = positive + 1
            if nums[i] < nums[i - 1]:
                positive = negative + 1
        return max(negative, positive)