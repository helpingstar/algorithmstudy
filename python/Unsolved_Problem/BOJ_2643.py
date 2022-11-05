import sys
import bisect
input = sys.stdin.readline

INF = 10000

n = int(input())
paper_list = []
for _ in range(n):
    a, b = map(int, input().split())
    paper_list.append((a, b) if a < b else (b, a))

paper_list.sort(key=lambda x: x[1])

board = [0] + [INF] * n

ans = 0
print(paper_list)
for a, _ in paper_list:
    pos = bisect.bisect_right(board, a)
    ans = max(ans, pos)
    board[pos] = a
    print(f'[board] {board}')

print(ans)
