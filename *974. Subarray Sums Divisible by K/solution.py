class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = [1] + [0] * k
        pre = 0
        ans = 0
        for num in nums:
            pre = (pre + num) % k
            ans += count[pre]
            count[pre] += 1
        
        return ans