class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        sum_map = {}
        sum_all = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                sum_all += 1
            else:
                sum_all -= 1
            
            if sum_all == 0:
                ans = i + 1
            elif sum_all in sum_map:
                ans = max(ans, i - sum_map[sum_all])
            else:
                sum_map[sum_all] = i
            
        return ans