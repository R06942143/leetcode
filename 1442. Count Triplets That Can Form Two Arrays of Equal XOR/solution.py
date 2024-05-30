class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        ans = 0

        for i in range(len(arr)):
            now = arr[i]
            for j in range(i+1, len(arr)):
                now ^= arr[j]
                if now == 0:
                    ans += (j-i)
        
        return ans