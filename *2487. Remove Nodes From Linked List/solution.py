# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head):
        prev = None
        current = head
        next_temp = None

        # Set each node's next pointer to the previous node
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the original linked list
        head = self.reverse_list(head)

        maximum = 0
        prev = None
        current = head

        # Traverse the list deleting nodes
        while current:
            maximum = max(maximum, current.val)

            # Delete nodes that are smaller than maximum
            if current.val < maximum:
                # Delete current by skipping
                prev.next = current.next
                deleted = current
                current = current.next
                deleted.next = None

            # Current does not need to be deleted
            else:
                prev = current
                current = current.next
        
        # Reverse and return the modified linked list
        return self.reverse_list(head)
