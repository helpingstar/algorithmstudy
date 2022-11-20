from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque()
        q.append((root, 0))
        while q:
            now, depth = q.popleft()
            if now is None:
                continue
            ans = max(depth+1, ans)
            q.append((now.left, depth+1))
            q.append((now.right, depth+1))
        return ans
