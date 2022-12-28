from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        check = set()
        while head.next is not None:
            if id(head) in check:
                return True
            check.add(id(head))
            head = head.next
        return False
