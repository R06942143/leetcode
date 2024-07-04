# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(1)
        dummy.next = head
        now = head

        while now.next:
            if now.val == 0 or now.next.val == 0:
                now = now.next
            else:
                now.val += now.next.val
                now.next = now.next.next
        
        remove_zero = dummy

        while remove_zero.next:
            if remove_zero.next.val == 0:
                remove_zero.next = remove_zero.next.next
            else:
                remove_zero = remove_zero.next

        
        return dummy.next
