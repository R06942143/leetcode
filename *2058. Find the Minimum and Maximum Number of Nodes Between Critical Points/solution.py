import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        if not head:
            return [-1, -1]
        
        
        ans = [math.inf, -math.inf]

        first_critical = None
        prev_critical = None

        prev = None
        now = head
        i = 0
        while now.next:
            if prev:
                if prev.val > now.val and now.next.val > now.val or prev.val < now.val and now.next.val < now.val:
                    if first_critical:
                        ans[0] = min(ans[0], i - prev_critical)
                        ans[1] = max(ans[1], i -first_critical)
                        prev_critical = i
                    else:
                        first_critical = i
                        prev_critical = i


            prev = now
            now = now.next
            i += 1

        if ans[0] != math.inf:
            return ans
        else:
            return [-1, -1]