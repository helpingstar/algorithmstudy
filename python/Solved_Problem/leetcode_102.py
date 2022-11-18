from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = [[]]
        q.append((root, 1))
        while q:
            now, depth = q.popleft()
            if now is None:
                continue

            if len(ans) == depth:
                ans.append([])
            ans[depth].append(now.val)

            if now.left:
                q.append((now.left, depth + 1))
            if now.right:
                q.append((now.right, depth + 1))
        return ans[1:]
