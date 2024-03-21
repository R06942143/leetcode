# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode| None) -> ListNode| None:
        if not head:
            return head
        pre = head
        now = head.next
        pre.next = None
        while now:
            following = now.next

            now.next = pre

            pre = now
            now = following
        
        return pre

