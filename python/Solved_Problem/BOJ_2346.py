import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    balls = list(map(int, input().split()))

    if N == 1:
        print(1)
        return

    visited = [False] * N
    visited[0] = True

    ans = [1]
    delta = balls[0]
    direction = -1 if delta < 0 else 1
    delta = abs(delta)
    cur = 0
    cnt = 1
    while N > cnt:
        while delta > 0:
            cur = (cur + direction) % N
            if not visited[cur]:
                delta -= 1
        ans.append(cur + 1)
        visited[cur] = True
        direction = -1 if balls[cur] < 0 else 1
        delta = abs(balls[cur])
        cnt += 1

    print(*ans)


solution()
