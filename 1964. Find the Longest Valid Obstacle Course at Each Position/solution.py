from bisect import bisect_right


class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: list[int]) -> List[int]:
        lis = []
        for i, x in enumerate(nums):
            if (
                len(lis) == 0 or lis[-1] <= x
            ):  # Append to LIS if new element is >= last element in LIS
                lis.append(x)
                nums[i] = len(lis)
            else:
                idx = bisect_right(lis, x)  # Find the index of the smallest number > x
                lis[idx] = x  # Replace that number with x
                nums[i] = idx + 1
        return nums
