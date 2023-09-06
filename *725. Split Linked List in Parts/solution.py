# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, root, k):
        parts = [None] * k

        len = 0
        node = root
        while node:
            len += 1
            node = node.next

        n, r = divmod(len, k)

        node = root
        prev = None

        for i in range(k):
            parts[i] = node

            for j in range(n + (1 if r > 0 else 0)):
                prev = node
                node = node.next

            if prev:
                prev.next = None

            if r > 0:
                r -= 1

        return parts