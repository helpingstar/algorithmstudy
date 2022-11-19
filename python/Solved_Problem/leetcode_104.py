from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        q.append((root, 0))
        while q:
            now, depth = q.popleft()

            if now is None:
                continue

            if len(ans) == depth:
                ans.append([])

            if depth % 2 == 0:
                ans[depth] = ans[depth] + [now.val]
            else:
                ans[depth] = [now.val] + ans[depth]

            if now.left is not None:
                q.append((now.left, depth+1))
            if now.right is not None:
                q.append((now.right, depth+1))

        return ans
