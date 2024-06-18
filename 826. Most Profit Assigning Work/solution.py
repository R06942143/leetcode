class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        array = [(difficulty[i], profit[i]) for i in range(len(profit))]

        array.sort(key = lambda x : x[0])
        worker.sort()
        total_profit = 0
        max_profit = 0
        j = 0
        for i in range(len(worker)):
            while j < len(array) and worker[i] >= array[j][0]:
                max_profit = max(max_profit, array[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit
