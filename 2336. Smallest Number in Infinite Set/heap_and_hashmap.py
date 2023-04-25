import heapq


# beats 97.8%
class SmallestInfiniteSet:
    def __init__(self):
        self.add_map = {}
        self.add_heap = []
        self.current = 1

    def popSmallest(self) -> int:
        if self.add_heap:
            answer = heapq.heappop(self.add_heap)
            del self.add_map[answer]
            return answer
        else:
            self.current += 1
            return self.current - 1

    def addBack(self, num: int) -> None:
        if not self.add_map.get(num) and num < self.current:
            self.add_map[num] = 1
            heapq.heappush(self.add_heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
