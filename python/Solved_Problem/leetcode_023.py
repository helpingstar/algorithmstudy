import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        
        for i, cur in enumerate(lists):
            if cur is None:
                continue
            heapq.heappush(q, (cur.val, i))
    
        if not q:
            return None
        
        value, index = heapq.heappop(q)
        head = h_cur = ListNode(value)
        
        if lists[index].next:
            lists[index] = lists[index].next
            heapq.heappush(q, (lists[index].val, index))
        
        while q:
            value, index = heapq.heappop(q)
            h_cur.next = ListNode(value)
            
            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(q, (lists[index].val, index))
            
            h_cur = h_cur.next
        return head