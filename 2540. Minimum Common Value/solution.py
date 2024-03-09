class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        set_nums1 = set(nums1)
        for num in nums2:
            if num in set_nums1:
                return num

        return -1