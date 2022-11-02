from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        board = [0] * (n+1)
        board[0] = 1
        for i in range(n-1):
            board[i+1] += board[i]
            board[i+2] += board[i]
        board[n] += board[n-1]

        return board[n]

a = Solution()
print(a.climbStairs(3))
