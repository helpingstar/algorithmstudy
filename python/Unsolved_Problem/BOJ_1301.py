import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    balls = [int(input()) for _ in range(N)]
    L = sum(balls)
    ans = 0
    def dp(pre1, pre2, cnt):
        nonlocal balls, L, ans, N
        if cnt == L:
            ans += 1
            return
        for i in range(N):
            if i == pre1 or i == pre2 or balls[i] == 0:
                continue
            balls[i] -= 1
            dp(pre2, i, cnt+1)
            balls[i] += 1
    dp(-1, -1, 0)
    print(ans)

solution()
