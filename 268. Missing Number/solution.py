class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        
        all_nums = set([i for i in range(n+1)])

        for num in nums:
            if num in all_nums:
                all_nums.remove(num)
        
        ans = all_nums.pop()

        return ans