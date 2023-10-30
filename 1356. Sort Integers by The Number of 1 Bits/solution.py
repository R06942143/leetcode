class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr