class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        index = 0
        total_time = 0
        while index < len(colors) - 1:
            if colors[index] != colors[index + 1]:
                index += 1
                continue
            
            if colors[index] == colors[index + 1]:
                start = index
                end = index
                current_time = neededTime[end]
                max_time = neededTime[end]
                while end + 1 < len(colors) and colors[end] == colors[end + 1]:
                    end += 1
                    current_time += neededTime[end]
                    max_time = max(max_time, neededTime[end])
                
                total_time += (current_time - max_time)

                index = end + 1
        
        return total_time