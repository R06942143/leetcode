from functools import lru_cache


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        n = len(events)
        events.sort()

        @lru_cache(None)
        def dp(end: int, event_index: int, k: int):
            if k == 0 or event_index == n:
                return 0

            event = events[event_index]
            event_start, event_end, event_value = event

            if event_start <= end:
                return dp(end, event_index + 1, k)

            attend = event_value + dp(event_end, event_index + 1, k - 1)
            skip = dp(end, event_index + 1, k)

            return max(attend, skip)

        dp.cache_clear()
        return dp(0, 0, k)
