from functools import cache

class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        answer = 0
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
            else:
                answer += self.countSubArray(zeros)
                zeros = 0
        return answer + self.countSubArray(zeros)
    @cache
    def countSubArray(self, zeros: int) -> int:
        return int(zeros*(zeros+1)/2)