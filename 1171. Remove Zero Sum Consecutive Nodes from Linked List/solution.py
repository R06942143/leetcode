# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        pre_sum_map = {}

        pre_sum = 0

        dummy = ListNode(next = head)
        now = dummy
        while now:
            pre_sum += now.val
            pre_sum_map[pre_sum] = now
            now = now.next
        
        now = dummy
        pre_sum = 0
        while now:
            pre_sum += now.val
            now.next = pre_sum_map[pre_sum].next
            now = now.next
        
        return dummy.next
    

    def solution2(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(next = head)

        start = dummy

        while start:
            pre = 0
            end = start.next

            while end:
                pre += end.val
                if pre == 0:
                    start.next = end.next
                end = end.next

            start = start.next
        
        return dummy.next