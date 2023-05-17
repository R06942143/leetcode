# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        # find N
        traversal = count = dummy = ListNode(next=head)
        n = 0
        while count.next:
            count = count.next
            n += 1

        stack = []
        t = 0
        ans = 0
        while traversal.next:
            traversal = traversal.next
            t += 1
            if t <= n / 2:
                stack.append(traversal.val)
            else:
                tmp = stack.pop()
                if ans < tmp + traversal.val:
                    ans = tmp + traversal.val

        return ans
        # mid = fast = dummy = ListNode(next=head)
        # ## find mid node O(n)
        # while fast.next and fast.next.next:
        #     mid = mid.next
        #     fast = fast.next.next

        # ## reverse node O(n)
        # new_head = mid
        # while new_head.next:
        #     tmp = new_head.next.next

        # mid.next = new_head
        # ## traversal sum O(n)
