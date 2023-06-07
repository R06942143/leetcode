class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numMap = {}
        i = 0
        for num in nums:
            if num in numMap:
                if i - numMap[num] <= k:
                    return True
            numMap[num] = i
            i += 1
        return False
