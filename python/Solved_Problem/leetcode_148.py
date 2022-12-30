import heapq
from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        q = []
        while head:
            heapq.heappush(q, head.val)
            head = head.next
        start = ListNode(heapq.heappop(q))
        prev = start
        while q:
            now = ListNode(heapq.heappop(q))
            prev.next = now
            prev = now
        return start
