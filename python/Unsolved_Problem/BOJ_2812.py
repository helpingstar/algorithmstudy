import sys

input = sys.stdin.readline
INF = int(1e6)
n, k = map(int, input().split())
size = k+1
num = input().rstrip()
ans = ''
cur = 0
while True:
    if size == 1:
        ans += num[cur:]
        break
    if n - cur == size-1:
        break

    max_value = int(num[cur])
    next_cur = cur
    for i in range(1, size):
        if int(num[cur+i]) > max_value:
            max_value = int(num[cur+i])
            next_cur = cur+i
    # print(f'[debug]  next_cur:{next_cur}, max_value:{max_value}')
    ans += str(num[next_cur])
    size -= (next_cur - cur)
    cur = next_cur+1

print(ans)
