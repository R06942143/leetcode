class Solution:
    def arraySign(self, nums: list[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0:
                return 0
            ans *= num
        if ans > 0:
            return 1
        else:
            return -1
