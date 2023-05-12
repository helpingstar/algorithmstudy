import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

lights = list(map(int, input().split()))

def check(h):
    if lights[0] - h > 0:
        return False
    if lights[-1] + h < N:
        return False
    for i in range(M-1):
        if (lights[i+1] - lights[i]) > (h + h):
            return False
    return True

l, r = 0, N
result = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        result = mid
        r = mid - 1
    else:
        l = mid + 1

print(result)
