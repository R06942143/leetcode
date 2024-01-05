from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ans = [nums[0]]
        for num in nums:
            if ans[-1] < num:
                ans.append(num)
            elif ans[-1] > num:
                ans[bisect_left(ans, num)] = num
        

        return len(ans)
