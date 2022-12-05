from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_index = 0
        self.count = 0
        self.inorder_index_map = {}
        for i, num in enumerate(inorder):
            self.inorder_index_map[num] = i

        def dfs(left, right):
            if right < left:
                return
            # print(f'[debug]  count:{self.count}, left:{left}, right:{right}')
            root_value = preorder[self.count]
            self.count += 1
            mid = self.inorder_index_map[root_value]
            root = TreeNode(root_value)
            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root

        return dfs(0, len(preorder)-1)
