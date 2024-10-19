from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        if not node1:
            return node2
        if not node2:
            return node1

        if node1.val < node2.val:
            return ListNode(node1.val, self.mergeTwoLists(node1.next, node2))
        return ListNode(node2.val, self.mergeTwoLists(node1, node2.next))
