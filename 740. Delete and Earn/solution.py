class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.all_map = {}
        for i in nums:
            if i in self.all_map:
                self.all_map[i] += i
            else:
                self.all_map[i] = i
        dp = [0 for i in range(max(self.all_map))]
        if self.all_map.get(1):
            dp[0] = self.all_map.get(1)
        if self.all_map.get(2):
            dp[1] = self.all_map.get(2)
        if len(dp) < 3:
            return max(dp)
        if self.all_map.get(3):
            dp[2] = self.all_map[3] + dp[0]
        else:
            dp[2] = dp[0]
        for i in range(3, len(dp)):
            if self.all_map.get(i + 1):
                now = self.all_map[i + 1]
            else:
                now = 0
            dp[i] = max(now + dp[i - 2], now + dp[i - 3])

        return max(dp[-1], dp[-2])
