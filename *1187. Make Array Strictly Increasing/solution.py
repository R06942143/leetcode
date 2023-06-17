import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2 = sorted(set(arr2))

        n1, n2 = len(arr1), len(arr2)

        d = {0: arr1[0]}

        if arr2[0] < arr1[0]:
            d[1] = arr2[0]

        for i in range(1, n1):
            new_d = {}
            x = arr1[i]

            for t, v in d.items():
                if v < x:
                    new_d[t] = x
            for t, v in d.items():
                idx = bisect.bisect_right(arr2, v)
                if idx < n2:
                    new_d[t + 1] = (
                        min(new_d[t + 1], arr2[idx]) if t + 1 in new_d else arr2[idx]
                    )
            d = new_d
            if not d:
                return -1
        return min(d.keys()) if d else -1
