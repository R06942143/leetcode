class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        i = -1
        for num in nums:
            i += 1
            rest = target - num
            if rest in seen:
                return [i, seen[rest]]
            seen[num] = i
