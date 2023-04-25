# only beat 5% QQ
class SmallestInfiniteSet:
    def __init__(self):
        self.pop_map = {}

    def popSmallest(self) -> int:
        i = 1
        while True:
            if not self.pop_map.get(i):
                self.pop_map[i] = 1
                return i
            i += 1

    def addBack(self, num: int) -> None:
        if self.pop_map.get(num):
            del self.pop_map[num]


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
