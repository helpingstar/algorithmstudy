from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        L = len(s)
        board = [[False] * L for _ in range(L)]
        self.ans = []

        for length in range(L):
            for start in range(L - length):
                end = start + length
                # print(f'[debug]  start:{start}, end:{end}')
                if length == 0:
                    board[start][end] = True
                else:
                    if s[start] == s[end]:
                        if length == 1:
                            board[start][end] = True
                        else:
                            # print(f'[debug]  start:{start}, end:{end}')
                            if board[start+1][end-1]:
                                board[start][end] = True
        # print(f'[debug]  board:{board}')
        def dp(start, arr):
            if start == L:
                self.ans.append(arr)
            for next in range(start, L):
                if board[start][next]:
                    dp(next+1, arr+[s[start:next+1]])
        dp(0, [])
        return self.ans
