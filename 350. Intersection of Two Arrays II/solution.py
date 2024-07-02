from collections import defaultdict


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        total_num = defaultdict(int)
        ans = []
        for num in nums1:
            total_num[num] += 1
        
        for num in nums2:
            if total_num[num] > 0:
                total_num[num] -= 1
                ans.append(num)
        
        return ans