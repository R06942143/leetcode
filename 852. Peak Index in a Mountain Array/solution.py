class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid - 1] <= arr[mid] and arr[mid] >= arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid
