from heapq import *

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        minCapitalHeap = []
        maxProfitHeap = []

        # Insert all capitals to a min-heap
        for i in range(0, len(profits)):
            heappush(minCapitalHeap, (capital[i], i))

        # Finding 'k' best projects
        availableCapital = w
        for _ in range(k):
            # Projects that can be selected within the available capital. Insert these in a max-heap
            while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
                capital, i = heappop(minCapitalHeap)
                heappush(maxProfitHeap, (-profits[i], i))

            # Break if we are not able to find any project that can be completed within the available capital
            if not maxProfitHeap:
                break

            # Add the profit from project with the maximum profit
            availableCapital += -heappop(maxProfitHeap)[0]

        return availableCapital