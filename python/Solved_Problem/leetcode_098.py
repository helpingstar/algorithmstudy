# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root:TreeNode, n_min, n_max):
            if root is None:
                return True
            if root.left is not None:
                left = root.left.val
            else:
                left = -(1<<32)

            if root.right is not None:
                right = root.right.val
            else:
                right = (1 << 32)

            return left < root.val < right and \
            n_min < root.val < n_max and \
            check(root.left, n_min, min(n_max, root.val)) and \
            check(root.right, max(n_min, root.val), n_max)

        return check(root, -(1<<32), (1 << 32))
