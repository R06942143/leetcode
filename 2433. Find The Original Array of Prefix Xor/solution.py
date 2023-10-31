class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        arr = [0] * len(pref)
        arr[0] = pref[0]
        for i in range(1, len(pref)):
            arr[i] = pref[i - 1]^pref[i]
        
        return arr
