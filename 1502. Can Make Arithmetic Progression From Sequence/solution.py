class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr = sorted(arr)
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != d:
                return False
        return True
