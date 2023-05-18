class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ans = []
        start = str(nums[0])
        end = ""
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                if end == "":
                    ans.append(start)
                else:
                    ans.append(start + "->" + end)
                if i < len(nums):
                    start = str(nums[i])
                    end = ""
                else:
                    start = ""
                    end = ""
            else:
                end = str(nums[i])
        if start != "":
            if end == "":
                ans.append(start)
            else:
                ans.append(start + "->" + end)
        return ans
