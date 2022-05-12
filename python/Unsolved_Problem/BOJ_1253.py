import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0

for i in range(n):
    tmp = arr[:i] + arr[i+1:]
    l, r = 0, len(tmp) -1

    while l < r:
        t = tmp[l] + tmp[r]
        if t == arr[i]:
            ans += 1
            break
        if t < arr[i]:
            l += 1
        else:
            r -= 1

print(ans)