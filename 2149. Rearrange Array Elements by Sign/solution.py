class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive_index = 0
        negative_index = 1
        ans = [0] * len(nums)
        for num in nums:
            if num > 0:
                ans[positive_index] = num
                positive_index += 2
            else:
                ans[negative_index] = num
                negative_index += 2
        
        return ans