class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        Sum = 0
        for num in nums:
            Sum ^= num
        
        ans = 0
        k ^= Sum 
        while k > 0:
            ans += k & 1
            k >>= 1
        
        return ans  