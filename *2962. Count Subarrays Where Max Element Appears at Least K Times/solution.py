class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_element = max(nums) # O(n)
        times = 0
        ans = 0
        start = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                times += 1
            
            while times == k:
                if nums[start] == max_element:
                    times -= 1
                start += 1
            
            ans += start
        
        return ans