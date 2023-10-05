class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        num_map = {}
        for num in nums:
            if num in num_map:
                num_map[num] +=1
            else:
                num_map[num] = 1
        ans = []
        for num, times in num_map.items():
            if times > len(nums) //3:
                ans.append(num)
        return ans