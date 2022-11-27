from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

INF = int(1e10)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # print(f'[debug]  {root}')
        self.ans = -INF
        def dp(now):
            if now.left:
                l_max = dp(now.left)
            else:
                l_max = -INF
            if now.right:
                r_max = dp(now.right)
            else:
                r_max = -INF

            self.ans = max((l_max+now.val, r_max+now.val, r_max+l_max+now.val, now.val, self.ans))
            # print(f'[debug]  l_max:{l_max}')
            # print(f'[debug]  r_max:{r_max}')
            # print(f'[debug]  now.val:{now.val}')
            # print(f'[deubg]  self.ans: {self.ans}')
            # print(f'[debug]  reutrn:{max((l_max+r_max, 0)) + now.val}')
            return max((l_max, r_max, 0)) + now.val
        dp(root)
        return self.ans
