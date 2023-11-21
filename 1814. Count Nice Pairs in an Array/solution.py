from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        diff_nums = [num - int(str(num)[::-1]) for num in nums]
        ans = 0
        modulor = 1000000007
        diff_map = defaultdict(int)
        for i in range(len(nums)):
            diff_map[diff_nums[i]] += 1
        
        for key, value in diff_map.items():
            if value > 1:
                ans += value* (value - 1)/2
        
        return int(ans % 1000000007)
    def countNicePairs_TLE(self, nums: list[int]) -> int:
        rev_nums = [int(str(num)[::-1]) for num in nums]
        ans = 0
        modulor = 1000000007
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + rev_nums[j] == rev_nums[i] + nums[j]:
                    ans += 1
        
        return ans % 1000000007