from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self.array = [[[-1, 0]] for _ in range(length)]
        self.current_snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.current_snap_id, val])

    def snap(self) -> int:
        self.current_snap_id += 1
        return self.current_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_right(self.array[index], snap_id, key=lambda x: x[0])
        return self.array[index][i - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
