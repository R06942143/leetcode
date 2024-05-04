class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        ans = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            ans += 1
            right -= 1
        return
