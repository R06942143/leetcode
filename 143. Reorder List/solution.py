# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Step one: find the mid node
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # Step two: reverse the second node
        pre = None
        now = slow.next
        slow.next = None
        while now:
            tmp = now.next
            now.next = pre
            pre = now
            now = tmp

        # Step three: merge two list
        now = head
        while now and pre:
            tmp = now.next
            tmp2 = pre.next
            now.next = pre
            pre.next = tmp
            now = tmp
            pre = tmp2
        
        return head

