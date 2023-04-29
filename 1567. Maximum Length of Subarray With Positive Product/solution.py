class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * 2

        if nums[0] > 0:
            dp[0] = 1

        if nums[0] < 0:
            dp[1] = 1

        res = dp[0]

        for i in range(1, n):
            cur = nums[i]
            tmp = [0] * 2
            if cur > 0:
                tmp[0] = dp[0] + 1
                if dp[1] > 0:
                    tmp[1] = max(tmp[1], dp[1] + 1)
            elif cur < 0:
                tmp[1] = dp[0] + 1
                if dp[1] > 0:
                    tmp[0] = max(tmp[0], dp[1] + 1)
            dp = tmp
            res = max(res, dp[0])

        return res

        """ error ans
        ans = 0
        positive = 0
        negative = 0
        dp = nums[0]
        if dp > 0:
            positive += 1
        elif dp < 0:
            negative += 1
        for i in range(1, len(nums)):
            print(dp, positive, negative)
            dp = dp * nums[i]
            if dp > 0:
                positive += 1
                positive = max(positive, negative + 1)
                negative = 0
            elif dp < 0:
                negative += 1
                negative = max(negative, positive + 1)
                positive = 0
            else:
                if i + 1 < len(nums):
                    dp = 1
                    if nums[i + 1] > 0:
                        positive = 1
                        negative = 0
                    elif nums[i + 1] < 0:
                        positive = 0
                        negative = 1
            ans = max(ans, positive)
        return ans
        """
