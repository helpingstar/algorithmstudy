class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horiozntal
        for i in range(9):
            check = set()
            for n in board[i]:
                if n == ".":
                    continue
                if n in check:
                    return False
                else:
                    check.add(n)

        for i in range(9):
            check = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] in check:
                    return False
                else:
                    check.add(board[j][i])

        for r in range(3):
            for c in range(3):
                check = set()
                for x in range(3):
                    for y in range(3):
                        if board[r*3 + x][c*3 + y] == ".":
                            continue
                        if board[r*3 + x][c*3 + y] in check:
                            return False
                        else:
                            check.add(board[r*3 + x][c*3 + y])
        return True
