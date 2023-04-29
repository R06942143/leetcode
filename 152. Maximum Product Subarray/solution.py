class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)

            res = max(res, curMax)

        return res

    """ TLE answer
        dp = [ [0] * len(nums) for _ in range(len(nums))]
        dp[0][0] = nums[0]
        ans = - float("inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j-1] * nums[j]
                if dp[i][j] > ans:
                    ans = dp[i][j]
        return ans
    """
