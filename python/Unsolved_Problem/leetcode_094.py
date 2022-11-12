from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []

        def InOrderTraversal(node):
            if node == None:
                return None

            InOrderTraversal(node.left)
            self.result.append(node.val)
            InOrderTraversal(node.right)

        InOrderTraversal(root)
        return self.result
