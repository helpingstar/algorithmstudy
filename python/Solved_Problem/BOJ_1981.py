import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

board = []
check_board = []
num_list = set()
for _ in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)
    check_board.append([0] * n)
    num_list = num_list.union(set(temp))
check_count = 1

num_list = sorted(list(num_list))
length = len(num_list)

def two_pointer():
    l, r = 0, 0
    ans = 300
    while l <= r < length:
        if bfs(num_list[l], num_list[r]):
            ans = min(ans, num_list[r] - num_list[l])
            # print(f'[DEBUG]  TRUE  | {l}, {r}')
            l += 1
        else:
            # print(f'[DEBUG]  FALSE | {l}, {r}')
            r += 1
    
    return ans
            
def bfs(left, right) -> bool:
    global check_count
    global check_board
    global n
    if not (left <= board[0][0] <= right):
        return False
    check_count += 1
    
    q = deque()
    q.append((0, 0))
    check_board[0][0] = check_count
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if check_board[nx][ny] == check_count:
                continue
            if not (left <= board[nx][ny] <= right):
                continue
            
            check_board[nx][ny] = check_count
            q.append((nx, ny))
    # print(f'[check_board] : {check_board}')
    # print(f'[length] : {length}')
    if check_board[n-1][n-1] == check_count:
        return True
    else:
        return False

print(two_pointer())