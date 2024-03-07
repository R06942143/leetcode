# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode|None) -> ListNode|None:
        dummy = ListNode(next = head)

        fast = slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            return slow.next
        else:
            return slow