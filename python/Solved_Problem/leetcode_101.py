from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):
            print(root1)
            print(root2)
            if root1 is None != root2 is None:
                return False

            if root1 is None and root2 is None:
                return True

            if root1 and root2:
                if root1.val != root2.val:
                    return False
                else:
                    one = dfs(root1.left, root2.right)
                    two = dfs(root1.right, root2.left)
                    return one and two
        if root:
            return dfs(root.left, root.right)
