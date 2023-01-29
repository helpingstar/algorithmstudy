import sys

input = sys.stdin.readline

def solution(n, board):
    M = [[[0] * 10 for j in range(1 << n)] for i in range(n)] # M[artist][path(bin)][price]

    def dfs(artist, path, price):
        if M[artist][path][price] != 0: # 메모제이션 적용
            return M[artist][path][price]

        count = 0 # 현재 artist 부터의 최대 거래 횟수
        for nextA in range(1, n):
            if board[artist][nextA] < price or path & (1 << nextA) > 0:
                continue
            count = max(count, 1 + dfs(nextA, path | (1 << nextA), board[artist][nextA]))
        M[artist][path][price] = count # 메모!

        return count

    return 1 + dfs(0, 1, 0)


n = int(input())
board = []
for i in range(n):
    board.append([int(j) for j in input().strip()])
result = solution(n, board)
print(result)
