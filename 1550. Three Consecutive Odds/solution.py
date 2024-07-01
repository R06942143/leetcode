class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        i = 0
        while i + 2 < len(arr):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i+ 2] % 2 == 1:
                return True
            i += 1
        
        return False