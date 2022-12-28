from typing import *

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        adr = dict()
        head_id = id(head)
        while head:
            if id(head) not in adr:
                adr[id(head)] = Node(head.val)
            if head.next is not None:
                if id(head.next) not in adr:
                    adr[id(head.next)] = Node(head.next.val)
                adr[id(head)].next = adr[id(head.next)]
            else:
                adr[id(head)].next = None

            if head.random is not None:
                if id(head.random) not in adr:
                    adr[id(head.random)] = Node(head.random.val)
                adr[id(head)].random = adr[id(head.random)]
            else:
                adr[id(head)].random = None

            head = head.next

        # for node in adr.values():
        #     print(node.val)
        return adr[head_id]
