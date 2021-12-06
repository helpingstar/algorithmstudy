from collections import deque

def bfs(num, queue):
    length = len(queue)
    m1 = [0, 0, 1, -1]
    m2 = [1, -1, 0, 0]
    for _ in range(length):
        x, y = queue.popleft()
        for k in range(4):
            x_new, y_new = x + m1[k], y + m2[k]
            if (0 <= x_new < n) and (0 <= y_new < n):
                 if not matrix[x_new][y_new]:
                     matrix[x_new][y_new] = num
                     queue.append((x_new, y_new))
            else:
                continue
        

n, k = map(int, input().split())
matrix = [list(map(int, (input().split()))) for _ in range(n)]
s, x1, y1 = map(int, input().split())

queue_list = [deque() for _ in range(k)]

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            queue_list[matrix[i][j] - 1].append((i, j))
            
for sec in range(s):
    for i in range(k):
        bfs(i+1, queue_list[i])

print(matrix[x1-1][y1-1])