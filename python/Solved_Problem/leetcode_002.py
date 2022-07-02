
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = '', ''
        while l1:
            a = str(l1.val) + a
            l1 = l1.next
        while l2:
            b = str(l2.val) + b
            l2 = l2.next
        
        result = str(int(a) + int(b))
        ans = ListNode()
        temp = ans
        for i in range(len(result)-1, -1, -1):
            temp.next = ListNode(int(result[i]))
            temp = temp.next
        return ans.next