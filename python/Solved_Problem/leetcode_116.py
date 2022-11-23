
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import *
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        count = 1
        if not root:
            return None
        if root.left is None:
            return Node(root.val, next=None)
        q = deque()
        q.append((root.left, 1))
        q.append((root.right, 1))
        prev = root
        while q:
            now, depth = q.popleft()
            # print(now.val)
            if count == (1 << depth) - 1:
                prev.next = None
            else:
                prev.next = now

            count += 1
            prev = now
            if now.left is None:
                continue
            q.append((now.left, depth+1))
            q.append((now.right, depth+1))
        return root
