from collections import defaultdict 


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
        
        nums.sort(reverse=True)
        nums.sort(key=lambda x: num_map[x])
        return nums