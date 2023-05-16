# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        now = dummy = ListNode(next=head)

        while now.next and now.next.next:
            first = now.next
            second = now.next.next

            first.next = second.next
            second.next = first
            now.next = second
            now = now.next.next

        return dummy.next
