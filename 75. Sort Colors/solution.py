class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
        
        for i in range(zeros):
            nums[i] = 0
        
        for i in range(ones):
            nums[i+zeros] = 1
        
        for i in range(len(nums) - zeros - ones):
            nums[i + zeros + ones] = 2
        
        return nums