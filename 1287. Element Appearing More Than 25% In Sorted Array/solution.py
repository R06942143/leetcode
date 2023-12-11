from collections import defaultdict
import bisect


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        num_count = defaultdict(int)
        goal = len(arr)//4
        for i in range(len(arr)):
            num_count[arr[i]] += 1
            if num_count[arr[i]] > goal:
                return arr[i]
    
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        
        for i in [n//4, n//2, 3*n//4, n]:
            if bisect.bisect_right(arr, arr[i]) - bisect.bisect_left(arr, arr[i]) > n//4:
                return arr[i]