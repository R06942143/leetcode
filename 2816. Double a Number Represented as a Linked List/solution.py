# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: ListNode | None) -> ListNode | None:
        def reverse_list(head: ListNode | None) -> ListNode | None:
            prev = None
            curr = head
            next_one = curr.next
            while next_one:
                curr.next = prev
                prev = curr
                curr = next_one
                next_one = next_one.next
            
            curr.next = prev
            return curr
        new_head = reverse_list(head)
        curr = new_head
        carry = 0
        while curr.next:
            new_val = (curr.val * 2) % 10 + carry
            carry = (curr.val * 2 )//10
            curr.val = new_val
            curr = curr.next
        
        new_val = (curr.val * 2) % 10 + carry
        carry = (curr.val * 2 )//10
        curr.val = new_val

        if carry:
            curr.next = ListNode(carry)
        return reverse_list(new_head)
        
