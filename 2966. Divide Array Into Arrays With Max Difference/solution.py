class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        ans = []
        tmp = []
        for i in range(len(nums)):
            if tmp and (nums[i] - tmp[-1] > k or nums[i] - tmp[0] > k):
                return []
            tmp.append(nums[i])
            if i % 3 == 2:
                ans.append(tmp)
                tmp = []
            
        return ans
