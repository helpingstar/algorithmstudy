from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dp(left, right):
            if left > right:
                return
            mid = (left+right) // 2

            root = TreeNode(nums[mid])

            root.left = dp(left, mid-1)
            root.right = dp(mid+1, right)

            return root
        return dp(0, len(nums)-1)
