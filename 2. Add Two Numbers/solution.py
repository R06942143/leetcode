# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        ans = dummy
        while l1 or l2 or carry:
            if not ans.next:
                ans.next = ListNode(0)
                ans = ans.next
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += carry
            carry = val // 10
            ans.val = val % 10
        return dummy.next
