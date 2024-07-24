class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def map_num(num):
            return int("".join(str(mapping[int(i)]) for i in str(num)))
        
        nums.sort(key=map_num)
    
        return nums
