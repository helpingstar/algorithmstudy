# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        cur = head
        length = 1
        while cur.next is not None:
            cur = cur.next
            length += 1

        if length == 1 or k % length == 0:
            return head

        k %= length
        k = length - k
        next_head = head
        for _ in range(k-1):
            next_head = next_head.next

        new_head = next_head.next
        next_head.next = None

        cur.next = head

        return new_head
