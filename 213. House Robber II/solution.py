class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        def helper(nums: list[int]) -> int:
            if len(nums) == 1 or len(nums) == 2:
                return max(nums)
            nums[2] += nums[0]
            for i in range(3, len(nums)):
                nums[i] = max(nums[i] + nums[i - 2], nums[i] + nums[i - 3])
            return max(nums[-1], nums[-2])

        return max(nums[0], nums[-1], helper(nums[1:]), helper(nums[:-1]))
