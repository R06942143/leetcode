from collections import deque, defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        ans = 0
        current_sum = 0
        array: deque[int] = deque()
        num_map: dict[int, int] = defaultdict(int)

        for i in range(k):
            array.append(nums[i])
            num_map[nums[i]] += 1
        current_sum = sum(array)

        if len(num_map.keys()) == k:
            ans = max(current_sum, ans)
        
        for i in range(k, len(nums)):
            to_be_removed = array.popleft()
            num_map[to_be_removed] -= 1
            if num_map[to_be_removed] == 0:
                del num_map[to_be_removed]
            
            array.append(nums[i])
            current_sum += (nums[i] - to_be_removed)
            num_map[nums[i]] += 1
            if len(num_map.keys()) == k:
                ans = max(current_sum, ans)
        
        return ans
        