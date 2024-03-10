class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_map = {}

        for num in nums1:
            nums1_map[num] = 1
        
        ans_map = {}

        for num in nums2:
            if num in nums1_map:
                ans_map[num] = 1
        
        return ans_map.keys()