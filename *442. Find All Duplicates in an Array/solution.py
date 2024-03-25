class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        rs = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                rs.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return rs