class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return [nums1_set.difference(nums2_set), nums2_set.difference(nums1_set)]

    def beautySolution(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
