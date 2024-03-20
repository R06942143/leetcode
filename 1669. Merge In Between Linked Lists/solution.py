# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_end = list2
        while list2_end.next:
            list2_end = list2_end.next
        
        list1_a = list1_b = list1

        while a > 1 and list1_a:
            list1_a = list1_a.next
            a -= 1
        
        while b > -1 and list1_b:
            list1_b = list1_b.next
            b -= 1

        list1_a.next = list2
        list2_end.next = list1_b

        return list1