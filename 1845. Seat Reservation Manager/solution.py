import heapq


class SeatManager:

    def __init__(self, n: int):
        self.now = 1
        self.available_seats = []

    def reserve(self) -> int:
        if self.available_seats:
            return heapq.heappop(self.available_seats)
        self.now += 1
        return self.now - 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)