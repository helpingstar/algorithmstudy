from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder_traversal(root):
            if root is None:
                return


            if root.left is not None:
                inorder_traversal(root.left)
            ans.append(root.val)
            if root.right is not None:
                inorder_traversal(root.right)
        inorder_traversal(root)
        return ans
