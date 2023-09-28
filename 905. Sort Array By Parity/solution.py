class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums) -1
        while l < r:
            if nums[r] % 2 == 0:
                if nums[l] %2 == 1:
                    tmp = nums[r]
                    nums[r] = nums[l]
                    nums[l] = tmp
                    l += 1
                else:
                    l += 1
            else:
                r -= 1
        return nums