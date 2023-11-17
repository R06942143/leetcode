class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums) - 1
        potential_ans = []
        for i in range(len(nums) // 2):
            potential_ans.append(nums[i] + nums[n -i])
        return max(potential_ans)