class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        total_a = 0
        total_b = 0
        for i in range(len(colors) - 2):
            if colors[i] == 'A' and colors[i + 1] == 'A' and colors[i + 2] == 'A':
                total_a += 1
            if colors[i] == 'B' and colors[i + 1] == 'B' and colors[i + 2] == 'B':
                total_b += 1
        
        return total_a > total_b