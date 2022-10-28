from typing import *
from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        q = deque()
        length = len(nums)
        visited = [False for _ in range(len(nums))]
        visited[0] = True
        cur = 0
        q.append(0)
        while q:
            now = q.popleft()
            i = min(length-now-1, nums[now])
            while i >= 1:
                next = now + i
                if not visited[next]:
                    if next == length - 1:
                        return True
                    q.append(next)
                    visited[next] = True
                i -= 1
        return False
