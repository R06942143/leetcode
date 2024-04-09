class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        i = 0
        ans = 0
        while tickets[k] != 0:
            if i == len(tickets):
                i = 0

            if tickets[i] > 0:
                tickets[i] -= 1
                i += 1
                ans += 1
            else:
                i += 1
        
        return ans