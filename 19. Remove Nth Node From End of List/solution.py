# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(val=0, next = head)
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        pre = dummy
        while fast:
            slow = slow.next
            fast = fast.next
            pre = pre.next
        
        pre.next = slow.next
        slow.next = None

        return dummy.next
