class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        num_map = {}
        ans = -1
        for num in nums:
            if num > 0:
                if -num in nums:
                    ans = max(ans, num)
                else:
                    num_map[num] = 1
            else:
                if -num in nums:
                    ans = max(ans, -num)
                else:
                    num_map[num] = 1
        
        return ans
