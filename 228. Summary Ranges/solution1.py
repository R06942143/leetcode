class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ans = []

        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start != end:
                    ans.append(str(start) + "->" + str(end))
                else:
                    ans.append(str(start))
                start = end = nums[i]
        if start != end:
            ans.append(str(start) + "->" + str(end))
        else:
            ans.append(str(start))

        return ans
