from collections import deque


class Solution:
    def minSwaps(self, s: str) -> int:
        q = deque()
        n_max = 0
        cnt = 0
        for b in s:
            if b == ']':
                cnt += 1
                n_max = max(n_max, cnt)
            else:
                cnt -= 1
        if n_max % 2 == 0:
            return n_max // 2
        else:
            return n_max // 2 + 1
