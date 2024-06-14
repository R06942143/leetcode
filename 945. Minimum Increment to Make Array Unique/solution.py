from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        num_array = defaultdict(int)
        for num in nums:
            num_array[num] += 1
        
        ordered_key = sorted(num_array.keys())
        ans = 0
        for key in ordered_key:
            if num_array[key] > 1:
                carry = (num_array[key] - 1)
                num_array[key] = 1
                current_key = key
                ans += carry
                while(carry != 0):
                    current_key += 1
                    carry = num_array[current_key] + carry - 1
                    num_array[current_key] = 1
                    ans += carry
        
        return ans
