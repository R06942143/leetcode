class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        ans = []
        for ppl in people:
            answer = 0
            for flower in flowers:
                if ppl >= flower[0] and ppl <= flower[1]:
                    answer += 1
            ans.append(answer)
        return ans