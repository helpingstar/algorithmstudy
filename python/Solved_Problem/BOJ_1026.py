import sys

input = sys.stdin.readline

n = int(input())
ans = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(key=lambda x: -x)

for i in range(n):
    ans += A[i] * B[i]

print(ans)
