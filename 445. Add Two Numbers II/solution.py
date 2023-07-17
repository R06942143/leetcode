# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        s1 = 0
        s2 = 0

        now1 = l1
        now2 = l2

        while now1 != None:
            s1 = s1 * 10 + now1.val
            now1 = now1.next

        while now2 != None:
            s2 = s2 * 10 + now2.val
            now2 = now2.next

        ans = str(s1 + s2)
        dummy = new = ListNode()
        for c in ans:
            nextOne = ListNode(val=int(c))
            new.next = nextOne
            new = new.next
        return dummy.next
