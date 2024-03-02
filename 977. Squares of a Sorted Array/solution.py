from collections import deque


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = []
        positive_nums = deque()
        negative_nums = deque()
        for num in nums:
            if num > 0:
                positive_nums.append(num**2)
            if num <= 0:
                negative_nums.appendleft(num**2)
        for _ in range(len(nums)):
            if positive_nums and negative_nums:
                if positive_nums[0] > negative_nums[0]:
                    ans.append(negative_nums.popleft())
                else:
                    ans.append(positive_nums.popleft())
            elif positive_nums:
                ans.extend(list(positive_nums))
                return ans
            else:
                ans.extend(list(negative_nums))
                return ans
        return ans
                
