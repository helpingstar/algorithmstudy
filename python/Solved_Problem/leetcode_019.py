# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        q = deque([head], maxlen=n+1)
        count = 1
        while cur.next:
            q.append(cur.next)
            cur = cur.next
            count += 1
        if n == 1:
            if count == 1:
                head = None
            else:
                q[0].next = None
        else:
            if count == n:
                head = q[1]
            else:
                q[0].next = q[2]
        return head
        