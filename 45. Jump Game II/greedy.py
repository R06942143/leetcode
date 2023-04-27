class Solution:
    def jump(self, nums: list[int]) -> int:
        now = 0
        count = 0
        while len(nums) > 1 and now < len(nums) - 1:
            largest = 0
            temp = 0
            for i in range(now, now + nums[now] + 1):
                if i >= len(nums) - 1:
                    return count + 1
                if i + nums[i] >= largest:
                    largest = i + nums[i]
                    temp = i
            now = temp
            count += 1

        return count
