# Definition for singly-linked list.
import bisect
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_list = []
        cur = head
        while cur:
            bisect.insort(num_list, cur.val)
            cur = cur.next
        if not num_list:
            return None
        head = cur = ListNode(num_list[0])
        for i in range(len(num_list)-1):
            cur.next = ListNode(num_list[i+1])
            cur = cur.next
        return head
