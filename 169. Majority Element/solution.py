class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ans = 0
        count = 0
        for num in nums:
            if count == 0:
                count += 1
                ans = num
            elif ans != num:
                count -= 1
            else:
                count += 1
        return ans
