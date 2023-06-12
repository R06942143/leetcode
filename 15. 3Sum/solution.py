class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                now = nums[l] + nums[r]
                if now > target:
                    r -= 1
                elif now < target:
                    l += 1
                else:
                    ans.add(tuple([nums[i], nums[l], nums[r]]))
                    r -= 1
                    l += 1

        return ans
