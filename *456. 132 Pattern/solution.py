import bisect


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        if not nums:
            return False
        
        afters = []
        
        min_i = [nums[0]]
        for i in range(1, len(nums)):
            min_i.append(min(min_i[-1], nums[i]))
        
        for j in reversed(range(len(nums))):
            if nums[j] > min_i[j]:
                index = bisect.bisect_left(afters, nums[j])
                if index > 0 and afters[index - 1] > min_i[j]:
                    return True
                bisect.insort_left(afters, nums[j])
        
        return False