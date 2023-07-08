class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        pairs = [0] * (len(weights) -1)
        for i in range(len(pairs)):
            pairs[i] = weights[i] + weights[i + 1]
        pairs.sort()
        return sum(pairs[len(pairs) - k + 1:]) - sum(pairs[:k-1])