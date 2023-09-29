class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return True
        direction = 0
        for i in range(len(nums)-1):
            if direction == 0:
                if nums[i] > nums[i+1]:
                    direction = 1
                elif nums[i] < nums[i + 1]:
                    direction = -1
            if direction == 1:
                if  nums[i] < nums[i + 1]:
                    return False
            
            if direction == -1:
                if nums[i] > nums[i+1]:
                    return False
        
        return True