import sys
import heapq
input = sys.stdin.readline


def solution():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    INF = int(1e9)
    ITER = 0
    while True:
        ITER += 1
        SIZE = int(input())
        if SIZE == 0:
            return
        board = [list(map(int, input().split())) for _ in range(SIZE)]
        dist = [[INF] * SIZE for _ in range(SIZE)]

        q = []
        heapq.heappush(q, (board[0][0], 0, 0))
        dist[0][0] = board[0][0]

        while q:
            cnt, r, c = heapq.heappop(q)

            if r == SIZE-1 and c == SIZE-1:
                break

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if not (0 <= nr < SIZE and 0 <= nc < SIZE):
                    continue
                if dist[r][c] + board[nr][nc] >= dist[nr][nc]:
                    continue
                heapq.heappush(q, (cnt + board[nr][nc], nr, nc))
                dist[nr][nc] = dist[r][c] + board[nr][nc]
        print(f"Problem {ITER}: {dist[SIZE-1][SIZE-1]}")


solution()
