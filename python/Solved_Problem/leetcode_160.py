from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        check = set()
        while not (headA is None and headB is None):
            if headA:
                if id(headA) in check:
                    return headA
                else:
                    check.add(id(headA))
                    headA = headA.next
            if headB:
                if id(headB) in check:
                    return headB
                else:
                    check.add(id(headB))
                    headB = headB.next
        return None
